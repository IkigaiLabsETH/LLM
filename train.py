"""Module for training a Llama 2 model using Replicate."""
import os
from dotenv import load_dotenv
import ai_chat

# Load environment variables from .env file
load_dotenv()

# Get API token from environment variable
api_token = os.getenv("REPLICATE_API_TOKEN")

if not api_token:
    raise ValueError("REPLICATE_API_TOKEN not found in environment variables")

# Set the API token
os.environ["REPLICATE_API_TOKEN"] = api_token

try:
    client = ai_chat.Client()
    training = client.trainings.create(
        version="meta/llama-2-70b-chat:"
                "02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
        input={
            "train_data": "https://huggingface.co/datasets/"
                          "livethelifetv/context",
            "num_train_epochs": 3
        },
        destination="ikigailabseth/ghost"
    )
    print(f"Training created successfully. ID: {training.id}")
except Exception as e:
    print(f"Error occurred: {type(e).__name__} - {e}")