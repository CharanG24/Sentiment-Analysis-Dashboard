# Sentiment Analysis Dashboard

A real-time sentiment analysis tool for monitoring social media posts or news articles, providing an insight into the sentiment behind the text.

Built using **Vue.js**, **Flask**, and **Natural Language Processing (NLP)** to analyze the text and provide sentiment results.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API](#api)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

This application allows you to analyze the sentiment of any given text input. The front-end is built with **Vue.js**, which sends the input text to a **Flask** backend. The backend processes the text using a basic **sentiment analysis algorithm** and returns a sentiment score (positive, negative, or neutral). The result is then displayed on the front-end in real-time.

---

## Tech Stack

- **Frontend:** 
  - Vue.js
  - Axios (for HTTP requests)
  - CSS3 (Styling)
  
- **Backend:** 
  - Flask
  - Python (for Sentiment Analysis)

- **Database:**
  - No database is required as the app only performs text sentiment analysis.

- **NLP:**
  - Custom sentiment analysis logic or any open-source NLP library like `TextBlob` or `VADER`.

---

## Features

- Real-time sentiment analysis of text input.
- Positive, negative, or neutral sentiment feedback based on the input.
- User-friendly interface with clear sentiment results.
- Easily extensible for future features, such as social media integration, advanced NLP models, or even storing past results.

---

## Prerequisites

- **Node.js** (for running Vue.js)
  - Download from [Node.js Official Website](https://nodejs.org/).
  
- **Python** (for running Flask API)
  - Download from [Python Official Website](https://www.python.org/).

- **Flask** and NLP library (for the backend)
  - Install Flask and your preferred NLP library using pip.

---

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

bash
Copy
Edit
npm install
Set up the backend:

Navigate to the backend directory:

bash
Copy
Edit
cd ../backend
Create a Python virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
Activate the virtual environment:

For Windows:

bash
Copy
Edit
venv\Scripts\activate
For macOS/Linux:

bash
Copy
Edit
source venv/bin/activate
Install required Python packages:

bash
Copy
Edit
pip install -r requirements.txt
Usage
1. Start the Backend (Flask API)
To run the Flask API locally, use the following command in the backend directory:

bash
Copy
Edit
python app.py
The backend will be running on http://localhost:5000.

2. Start the Frontend (Vue.js App)
To run the Vue.js app locally, use the following command in the frontend directory:

bash
Copy
Edit
npm run serve
The frontend will be accessible at http://localhost:8080.
