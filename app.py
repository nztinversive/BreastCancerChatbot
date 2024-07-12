from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data['message']
    
    # This is where you would integrate with your LLM or AI model
    # For now, we'll just echo back a simple response
    ai_response = f"I received your message: '{user_message}'. As an AI assistant, I'm here to help with breast cancer care information. How can I assist you further?"
    
    return jsonify({'response': ai_response})

if __name__ == '__main__':
    app.run(debug=True)
