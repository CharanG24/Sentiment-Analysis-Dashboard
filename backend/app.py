from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# Root route for Render or simple status check
@app.route('/')
def home():
    return 'Sentiment Analysis API is live!'

# Optional: health check route
@app.route('/health')
def health():
    return 'OK', 200

# Sentiment analysis route
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    blob = TextBlob(text)
    sentiment = {
        'polarity': blob.sentiment.polarity,
        'subjectivity': blob.sentiment.subjectivity
    }
    return jsonify(sentiment)

if __name__ == '__main__':
    app.run(debug=True)
