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
        assistant_reply = response['choices'][0]['message']['content']
        print(assistant_reply)
        return jsonify({"response": response['choices'][0]['message']['content']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
