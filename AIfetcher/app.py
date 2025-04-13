from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai


import os

# Get path to the parent directory (AI_Chatbot/)
base_dir = os.path.dirname(os.path.dirname(__file__))
key_path = os.path.join(base_dir, "apikeys.txt")

with open(key_path) as f:
    lines = f.readlines()
    api_key = lines[5].strip()  # line 6 (index 5)



app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Set your Gemini API Key

genai.configure(api_key="AIzaSyCShjJfSgtqGMMnqC73g094mLScv1L4bHA")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json  # Expecting JSON data
    user_message = data.get('message', '')

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")  # Use Gemini Pro Model
        response = model.generate_content(user_message)

        bot_reply = response.text if response else "No response from AI."
        return jsonify({"reply": bot_reply})
    
    except Exception as e:
        return jsonify({"reply": "Error: " + str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Running Flask on port 5001