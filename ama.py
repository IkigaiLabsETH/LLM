import requests
import os
import json
import time

# Set your Replicate API token directly in the script
API_TOKEN = ""

headers = {
    "Authorization": f"Token {API_TOKEN}",
    "Content-Type": "application/json"
}

# The correct endpoint URL for creating predictions
URL = "https://api.replicate.com/v1/predictions"


def ask_question(user_question):
    """Send a question to the AI model and return the response."""
    # Define the input data
    input_data = {
        "input": {
            "prompt": user_question
        },
        "version": "meta/llama-2-70b-chat" 
    }

    # Remove any 'id' field if it exists
    input_data.pop('id', None)

    try:
        # Make the API request
        response = requests.post(
            URL,
            headers=headers,
            json=input_data
        )
        response.raise_for_status()
        prediction = response.json()

        # Poll for the result
        while prediction['status'] not in ['succeeded', 'failed']:
            time.sleep(1)
            response = requests.get(f"{URL}/{prediction['id']}", timeout=30)
            response.raise_for_status()
            prediction = response.json()

        if prediction['status'] == 'succeeded':
            return prediction['output']
        else:
            return f"Error: {prediction['error']}"

    except requests.exceptions.HTTPError as e:
        error_message = e.response.json()
        return (f"Error: {e.response.status_code} - "
                f"{json.dumps(error_message, indent=2)}")

if __name__ == "__main__":
    question = input("Enter your question: ")
    answer = ask_question(question)
    print("Answer:", answer)
