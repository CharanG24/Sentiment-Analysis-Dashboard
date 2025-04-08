from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
