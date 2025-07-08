# 📚 Book Recommendation System using KNN + Streamlit

import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# ===== 1. Load Data =====
@st.cache_data
def load_data():
    ratings = pd.read_csv("ratings.csv")
    books = pd.read_csv("books.csv")
    return ratings, books

ratings, books = load_data()

# ===== 2. Preprocess Data =====
book_ratings = ratings.merge(books, on='bookId')

# Filter popular books (≥2 ratings) and active users (≥2 ratings)
popular_books = book_ratings.groupby('title')['rating'].count().reset_index()
popular_books = popular_books[popular_books['rating'] >= 1]['title']
filtered_data = book_ratings[book_ratings['title'].isin(popular_books)]

user_rating_count = filtered_data.groupby('userId')['rating'].count().reset_index()
active_users = user_rating_count[user_rating_count['rating'] >= 2]['userId']
filtered_data = filtered_data[filtered_data['userId'].isin(active_users)]

# Pivot table: rows = books, cols = users
book_pivot = filtered_data.pivot_table(index='title', columns='userId', values='rating').fillna(0)

# ===== 3. Train KNN Model =====
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(book_pivot.values)

# ===== 4. Recommend Function =====
def recommend_books(book_name, n=5):
    if book_name not in book_pivot.index:
        return []
    n = min(n + 1, len(book_pivot))  # Ensure n_neighbors doesn't exceed data
    book_index = book_pivot.index.get_loc(book_name)
    distances, indices = model.kneighbors([book_pivot.iloc[book_index].values], n_neighbors=n)

    recommended_books = []
    for i in range(1, len(distances[0])):  # skip the input book itself
        title = book_pivot.index[indices[0][i]]
        cover = get_cover_image(title)
        recommended_books.append((title, cover))
    return recommended_books

# ===== 5. Get Cover Image =====
def get_cover_image(title):
    row = books[books['title'] == title]
    if not row.empty:
        return row.iloc[0]['image_url']
    return "https://via.placeholder.com/120x180.png?text=No+Image"

# ===== 6. Streamlit UI =====
st.set_page_config(page_title="Book Recommender", page_icon="📚")
st.title("📚 Book Recommendation System")

selected_book = st.selectbox("Select a book you like:", book_pivot.index)

if st.button("Recommend"):
    results = recommend_books(selected_book)
    if results:
        st.subheader("📖 You may also like:")
        cols = st.columns(len(results))
        for i, (title, img) in enumerate(results):
            with cols[i]:
                st.image(img, width=120)
                st.caption(title)
    else:
        st.warning("No recommendations found.")
