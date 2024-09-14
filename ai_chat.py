import gradio as gr
import ai_chat
import os

# Ensure you have set the REPLICATE_API_TOKEN environment variable
os.environ["REPLICATE_API_TOKEN"] = ""

# Function to generate response using Replicate API
def predict(message, history):
    messages = [f"Human: {item[0]}\nAI: {item[1]}" for item in history]
    messages.append(f"Human: {message}")
    prompt = "\n".join(messages)

    # Use Replicate API to generate response
    output = ai_chat.run(
        "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",  # Replace with the actual model version
        input={"prompt": prompt}
    )

    # The output is typically a generator, so we need to join the chunks
    response = "".join(output)

    return response

# Create and launch the Gradio interface
gr.ChatInterface(predict).launch(share=True)