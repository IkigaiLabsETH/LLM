"""Module for interacting with the Replicate API."""

import os
import requests

def get_prediction(prediction_id):
    """Fetch a prediction from the Replicate API."""
    base_url = "https://api.replicate.com/v1/predictions"
    url = f"{base_url}/{prediction_id}"
    
    token = os.getenv('REPLICATE_API_TOKEN')
    if not token:
        raise ValueError("REPLICATE_API_TOKEN not found in environment variables")

    headers = {
        "Authorization": f"Token {token}"
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching prediction: {e}")
        return None

if __name__ == "__main__":
    prediction_id = ""
    result = get_prediction(prediction_id)
    if result:
        print(result)
