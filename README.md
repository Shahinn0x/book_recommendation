# 📚 Book Recommendation System using KNN + Streamlit

![Screenshot 2025-07-08 174942](https://github.com/user-attachments/assets/0238f18d-b9f4-418d-8b05-aaff93794317)

This project is a **Book Recommendation System** built using **Collaborative Filtering** with the **K-Nearest Neighbors (KNN)** algorithm. It uses a simple and engaging **Streamlit interface** to allow users to select a book they like and get recommendations for similar books based on user rating patterns.

---

## 🚀 Features

- 🔍 Select a book and get similar suggestions
- 🤝 Uses collaborative filtering (user-book matrix)
- 📈 Powered by KNN using cosine similarity
- 🧠 Efficient for small-to-medium datasets
- 🖼️ Displays book covers dynamically (with fallback image)
- 🧪 Interactive UI built with Streamlit

---

## 🧠 Technologies Used

| Technology     | Purpose                                 |
|----------------|------------------------------------------|
| **Python**     | Core programming language                |
| **pandas**     | Data preprocessing and manipulation      |
| **scikit-learn** (KNN) | ML algorithm for recommendation     |
| **Streamlit**  | Web UI framework                         |

---

## 📁 Project Structure

book-recommendation-system/
│
├── app.py # Streamlit app with all logic
├── books.csv # Book metadata with image URLs
├── ratings.csv # User rating data
├── requirements.txt # List of Python dependencies
└── README.md # You're reading this!


---

## 📥 Dataset Description

- `books.csv`:
  - `bookId`, `title`, `authors`, `image_url`
- `ratings.csv`:
  - `userId`, `bookId`, `rating`

You can use your own dataset or download one from:
- 📦 [Book-Crossing Dataset on Kaggle](https://www.kaggle.com/datasets/ruchi798/bookcrossing-dataset)

---

## 🔧 How It Works

1. Loads and merges the datasets
2. Filters popular books and active users
3. Creates a **pivot table** (books × users)
4. Trains a **KNN model** using cosine similarity
5. When a book is selected, KNN finds similar books
6. Displays the recommended books with their covers

---

## ▶️ How to Run

### ✅ Step 1: Install requirements

```bash
pip install -r requirements.txt

streamlit run app.py

