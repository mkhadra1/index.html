from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


# Replace YOUR_API_KEY with your OpenAI API key
openai.api_key = "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"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are NeuralRogue, a fun and edgy AI assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        print("OpenAI response:", response)  # Debug print to check response content
        assistant_reply = response['choices'][0]['message']['content']
        return jsonify({"response": assistant_reply})
    except Exception as e:
        print("Error occurred:", e)  # Debug print for error details
        return jsonify({"error": str(e)}), 500
    

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
