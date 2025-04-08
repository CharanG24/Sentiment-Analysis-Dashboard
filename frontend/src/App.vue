<template>
  <div id="app">
    <div class="container">
      <h1 class="title">Sentiment Analysis Dashboard</h1>
      <div class="input-container">
        <input 
          v-model="inputText" 
          placeholder="Type something..." 
          class="input-field"
          type="text"
        />
        <button @click="analyzeSentiment" class="analyze-btn">Analyze</button>
      </div>
      <div v-if="sentiment !== null" class="result">
        <p class="sentiment-text">
          Sentiment Score: <strong>{{ sentiment }}</strong>
        </p>
        <p v-if="sentiment === 0" class="neutral">This text has a neutral tone.</p>
        <p v-else-if="sentiment > 0" class="positive">This text has a positive sentiment!</p>
        <p v-else class="negative">This text has a negative sentiment.</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputText: '',
      sentiment: null,
    }
  },
  methods: {
    async analyzeSentiment() {
      const response = await fetch('https://your-backend-yx3u.onrender.com', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: this.inputText }),
      });
      const data = await response.json();
      this.sentiment = data.sentiment;
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f1f2f6;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  color: #333;
}

.container {
  text-align: center;
  background-color: white;
  padding: 50px;
  border-radius: 12px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 500px;
}

.title {
  font-size: 28px;
  margin-bottom: 30px;
  color: #2c3e50;
  font-weight: 600;
}

.input-field {
  padding: 12px;
  width: 80%;
  max-width: 350px;
  border: 2px solid #ccc;
  border-radius: 8px;
  font-size: 16px;
  margin-bottom: 15px;
  transition: all 0.3s ease;
}

.input-field:focus {
  border-color: #6c93f1;
  outline: none;
}

.analyze-btn {
  padding: 12px 25px;
  background-color: #6c93f1;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s, transform 0.3s;
}
.analyze-btn:hover {
  background-color: #45a049;
}

.result {
  margin-top: 20px;
  font-size: 18px;
}

.sentiment-text {
  font-weight: bold;
}

.positive {
  color: #28a745;
}

.negative {
  color: #dc3545;
}

.neutral {
  color: #6c757d;
}

</style>
