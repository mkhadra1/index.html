from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace YOUR_API_KEY with your OpenAI API key
openai.api_key = "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
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
        return jsonify({"response": response['choices'][0]['message']['content']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
