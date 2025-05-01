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

📊 Sentiment Classification Report:
              precision    recall  f1-score   support

    negative       1.00      1.00      1.00         1
     neutral       0.50      1.00      0.67         1
    positive       1.00      0.67      0.80         3

    accuracy                           0.80         5
   macro avg       0.83      0.89      0.82         5
weighted avg       0.90      0.80      0.81         5
