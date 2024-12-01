from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
from openai import OpenAI
import os
# from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

# load_dotenv()
api_key = os.getenv("API_KEY")

# Replace YOUR_API_KEY with your OpenAI API key
client = OpenAI(
    api_key = api_key
)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get the user message
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Send the message to OpenAI API
        response = client.chat_completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are NeuralRogue, a fun and edgy AI assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        # Check the response from OpenAI
        if not response or "choices" not in response:
            return jsonify({"error": "Invalid response from OpenAI"}), 500

        assistant_reply = response.choices[0].message.content.strip()
        return jsonify({"response": assistant_reply})
    except Exception as e:
        # Log the error for debugging
        print("Error occurred:", e)
        return jsonify({"error": str(e)}), 500
    

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
