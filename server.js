const express = require('express');
const path = require('path');
const axios = require('axios');

const app = express();
const port = 3000;

// Serve static files from the "public" folder
app.use(express.static("public"));
app.use(express.json()); // Middleware to parse JSON requests

// Serve HTML pages
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, "main_page.html"));
});

app.get('/login', (req, res) => {
    res.sendFile(path.join(__dirname, "login.html"));
});

app.get('/signup', (req, res) => {
    res.sendFile(path.join(__dirname, "signup.html"));
});

// Chatbot API route (Forwards to Flask)
const FLASK_API_URL = "https://ai-chatbot-2io2.onrender.com/chat";

app.post('/chat', async (req, res) => {
    try {
        const response = await axios.post(FLASK_API_URL, req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ reply: "Error connecting to AI model." });
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
