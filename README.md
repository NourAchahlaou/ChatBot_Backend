# Flask Chatbot Application README

## Overview

This README provides instructions for setting up and running a Flask application that serves as a chatbot using the Groq API. The chatbot is designed to offer insights and guidance on the health and wellness of senior citizens.

## Prerequisites

Before you can run the application, make sure you have the following installed:

* Python 3.7 or higher
* pip (Python package installer)
* virtualenv (for creating isolated Python environments)

## Setup Instructions
1. Clone the Repository
    If you haven't already, clone the repository to your local machine:

    `git clone <repository_url>
    cd <repository_directory>`


2. Create a Virtual Environment
    Create a virtual environment to manage dependencies:

   `python -m venv venv`

3. Activate the Virtual Environment

    On Windows:
    
   `venv\Scripts\activate`
    On macOS/Linux:

    `source venv/bin/activate`
4. Install Dependencies
    Install the required Python packages using pip:

    `pip install -r requirements.txt`

5. Set the Groq API Key
Set the Groq API key in your environment variables. You can do this by creating a .env file in the root directory of the project and adding the following line:

`GROQ_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxx`

Alternatively, you can export the environment variable directly in your terminal session:
  On Windows:
    
  `set GROQ_API_KEY=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`
  On macOS/Linux:
    
  `export GROQ_API_KEY=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`

## Running the Application
1. Start the Flask Server
Run the Flask development server:
   `python app.py`
The application should now be running at http://127.0.0.1:5000/.
2. Test the Chatbot
You can test the chatbot by sending a POST request to the /chat endpoint with a JSON payload containing the user's prompt. For example:


`curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"prompt": "How can I improve my grandmother's diet?"}'`
The response will be a JSON object containing the chatbot's reply.

## Project Structure

app.py: Main application file containing the Flask server and chatbot logic.
requirements.txt: List of Python dependencies required for the project.



Acknowledgements
This project uses the Groq API to generate responses and Flask to serve the web application. Special thanks to the developers of these tools.

Contact
For questions or feedback, please contact achahlaou.nour@gmail.com.






