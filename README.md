# Sentiment Analysis Dashboard

A real-time sentiment analysis tool for monitoring social media posts or news articles, providing an insight into the sentiment behind the text.

Built using **Vue.js**, **Flask**, and **Natural Language Processing (NLP)** to analyze the text and provide sentiment results.

Link: https://sentiment-analysis-dashboard-sable.vercel.app/

<img width="1037" alt="image" src="https://github.com/user-attachments/assets/437bf868-c771-4b4b-919c-c1784f098d09" />


## Project Overview

This application allows you to analyze the sentiment of any given text input. The front-end is built with **Vue.js**, which sends the input text to a **Flask** backend. The backend processes the text using a basic **sentiment analysis algorithm** and returns a sentiment score (positive, negative, or neutral). The result is then displayed on the front-end in real-time.

## Tech Stack

- **Frontend:** 
  - Vue.js
  - Axios (for HTTP requests)
  - CSS3 (Styling)
  
- **Backend:** 
  - Flask
  - Python (for Sentiment Analysis)

- **NLP:**
  - open-source NLP library  `TextBlob`

## Features

- Real-time sentiment analysis of text input.
- Positive, negative, or neutral sentiment feedback based on the input.
- User-friendly interface with clear sentiment results.
- Easily extensible for future features, such as social media integration, advanced NLP models, or even storing past results.


## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/sentiment-analysis-dashboard.git
cd sentiment-analysis-dashboard
```


Set up the frontend: 

Navigate to the frontend directory:

```bash
cd frontend
```
Install dependencies:

```bash
npm install
```

Set up the backend:

Navigate to the backend directory:

```bash
cd ../backend
```

Create a Python virtual environment (optional but recommended):

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Install required Python packages:

```bash
pip install -r requirements.txt
```

Usage
1. Start the Backend (Flask API)
To run the Flask API locally, use the following command in the backend directory:

```bash
python app.py
The backend will be running on http://localhost:5000.
```

2. Start the Frontend (Vue.js App)
To run the Vue.js app locally, use the following command in the frontend directory:

```bash
npm run serve
The frontend will be accessible at http://localhost:8080.
```
