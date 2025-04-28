# 🎌 Anime Recommendation System

This project is an **Anime Recommendation System** that helps users find similar anime based on the one they select. 

 
It uses **sentence-transformers embeddings**, **K-Nearest Neighbors (KNN)** for similarity search, and a beautiful **Streamlit web app** for the interface.

---

## 📋 Project Structure

```
├── anime_data.csv           # Preprocessed Anime Data
├── anime_embeddings.pkl     # Sentence embeddings of 'tags'
├── anime_knn_model.pkl      # Trained KNN model
├── model_creation.ipynb     # Notebook to create and save model artifacts
├── app.py                   # Streamlit app to interact with the model
└── README.md                # This file
```

---

## 🚀 Features

- Select anime by **Original Name** or **English Name**.
- Get **top 10 similar anime** recommendations.
- View details like:
  - Name
  - English Name
  - Genres
  - Synopsis
  - Type
  - Episodes
  - Aired Dates
  - Status
  - Studios
  - Source
  - Duration
  - Rating
- Beautiful **recommendation tiles** with:
  - **Anime posters**
  - **Hover animation** (optional)
  - **Clickable anime titles** (optional if you add external links)
- Clean **2-column layout** for details.
- Fast **semantic search** powered by **Sentence Transformers** and **KNN**.

---

## 🛠️ Tech Stack

- Python 3.11+
- pandas
- scikit-learn
- sentence-transformers
- pickle
- Streamlit
- Requests

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SHIGINVP/Anime-Recommendation-System.git
   cd Anime-Recommendation-System
   ```
2. (Recommended) Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

- On **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- On **Linux/Mac**:

  ```bash
  source venv/bin/activate
  ```



3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```



---

## ⚙️ How to Run

1. First, generate embeddings and KNN model:
   - Open and run `model_creation.ipynb`.
   - It will save:
     - `anime_embeddings.pkl`
     - `anime_knn_model.pkl`
     - `anime_data.csv`
   
2. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---



## 🙌 Acknowledgements

- [Sentence Transformers](https://www.sbert.net/)
- [Streamlit](https://streamlit.io/)
- [MyAnimeList Dataset](https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset) 

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and share it!

---

# ✨ Happy Recommending! 🎌🎉
