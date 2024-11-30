from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

api_key = os.getenv("API_KEY")

# Replace YOUR_API_KEY with your OpenAI API key
client = OpenAI(
    api_key = api_key
)
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are NeuralRogue, a fun and edgy AI assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        print("OpenAI response:", response)  # Debug print to check response content
        assistant_reply = response.choices[0].message.content.strip()
        return jsonify({"response": assistant_reply})
    except Exception as e:
        print("Error occurred:", e)  # Debug print for error details
        return jsonify({"error": str(e)}), 500
    

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
