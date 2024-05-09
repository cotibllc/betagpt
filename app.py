from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    model = data['model']
    message = data['message']

    if model == 'openai':
        # Make API request to OpenAI
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers={'Authorization': f'Bearer {OPENAI_API_KEY}'},
            json={'model': 'gpt-3.5-turbo', 'messages': [{'role': 'user', 'content': message}]}
        )
        result = response.json()['choices'][0]['message']['content']
    elif model == 'claude':
        # Make API request to Claude Opus
        response = requests.post(
            'https://api.anthropic.com/v1/chat',
            headers={'Authorization': f'Bearer {ANTHROPIC_API_KEY}'},
            json={'model': 'opus', 'messages': [{'role': 'user', 'content': message}]}
        )
        result = response.json()['choices'][0]['text']
    elif model == 'gemini':
        # Make API request to Gemini 1.0
        response = requests.post(
            'https://api.gemini.com/v1/chat',
            headers={'Authorization': f'Bearer {GEMINI_API_KEY}'},
            json={'model': 'gemini-1.0', 'messages': [{'role': 'user', 'content': message}]}
        )
        result = response.json()['choices'][0]['text']

    return jsonify({'response': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443)