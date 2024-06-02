from flask import Flask, request, jsonify
from groq import Groq
import os
import json
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
# Initialize Groq client
client = Groq(api_key=os.getenv('GROQ_API_KEY'))
MODEL = 'llama3-70b-8192'

def generate_chatbot_response(user_prompt):
    """Generate a response to the user's prompt using Groq."""
    # Prepare messages for Groq chat completion
    messages = [
        {"role": "user", "content": user_prompt},
        {"role": "system", "content": "Connect with me in my capacity as a seasoned medical practitioner dedicated to the comprehensive care of senior citizens, prioritizing their holistic wellness encompassing mental and physical health. Feel free to discuss any inquiries or concerns pertaining to the health and vitality of the elderly community. I offer personalized insights and guidance tailored to their distinct needs and circumstances, including advice on diseases and potential treatment options where available."}
    ]

    # Define the tool to call the Groq function
    tools = [{"type": "text", "content": user_prompt}]

    # Generate completion using Groq
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        tool_choice="auto",
        max_tokens=150
    )

    # Extract and return the response from Groq
    return response.choices[0].message.content

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_prompt = request.json.get('prompt', '')
        if not user_prompt:
            return jsonify({'error': 'Missing prompt parameter'}), 400
        response = generate_chatbot_response(user_prompt)
        return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
