# 📰 News Sentiment Analyzer

This project analyzes recent news articles related to a given company and predicts the overall sentiment (positive, neutral, or negative) using a machine learning model.

## 🚀 Overview

- 🧠 **ML Model**: Naive Bayes (scikit-learn) trained on labeled financial phrases.
- 🔍 **Data Source**: NewsAPI.org
- 💡 **Use Case**: For companies and analysts to gauge public sentiment from recent news.
- 🌐 **Architecture**: Flask (backend) + React (frontend) + TensorFlow (optional)

---

## 🛠️ Tech Stack

| Component     | Tech                     |
|---------------|--------------------------|
| Frontend      | React (TypeScript)       |
| Backend       | Python + Flask + Flask-CORS |
| ML Frameworks | scikit-learn, NLTK, NumPy |
| APIs          | NewsAPI.org              |

---

## 📦 Project Structure

```bash
news-sentiment-analysis/
├── backend/
│   ├── api/
│   ├── models/
│   ├── utils/
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
├── .gitignore
├── README.md
└── requirements-dev.txt

## 🔧 Setup Instructions

### 🐍 Backend Setup (Flask API)

1. Create and activate a virtual environment:

   python3.10 -m venv tfenv
   source tfenv/bin/activate

2. Install dependencies:

pip install -r requirements.txt

3. Create a .env file in the project root with your News API key:

NEWS_API_KEY=your_api_key_here

4. Run the Flask server:

python backend/app.py

You should see output like:

DEBUG: NEWS_API_KEY = your_api_key_here
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

🌐 Frontend Setup (React App)

1. Navigate to the frontend folder:

cd frontend

2. Install packages:

npm install

3. Start the development server:

npm start

The React app should open at:

http://localhost:3000/

🧪 Notes
Python version used: 3.10
TensorFlow for Mac (Apple Silicon): tensorflow-macos
Do not include .env or tfenv/ in your Git or submission zip.
For model evaluation, see the 📊 Model Evaluation section below.

📊 Model Evaluation

Sentiment Classification Report:
              precision    recall  f1-score   support

    negative       1.00      1.00      1.00         1
     neutral       0.50      1.00      0.67         1
    positive       1.00      0.67      0.80         3

    accuracy                           0.80         5
   macro avg       0.83      0.89      0.82         5
weighted avg       0.90      0.80      0.81         5
