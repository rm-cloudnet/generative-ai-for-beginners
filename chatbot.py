import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from .env file
load_dotenv()

# Get your Hugging Face API key
hf_token = os.getenv("HUGGING_FACE_API_KEY")

# Initialize the lightweight inference client
client = InferenceClient(token=hf_token)

# Use a highly capable conversational model
model_id = "HuggingFaceH4/zephyr-7b-beta"

# Take input from the user
user_query = input("Ask your question: ")

# Define the conversation with the user's input
messages = [
    {"role": "system", "content": "You are a concise, helpful assistant."},
    {"role": "user", "content": user_query}
]

# Generate the chat completion using the remote API
completion = client.chat_completion(
    model=model_id,
    messages=messages,
    max_tokens=300,
    temperature=0.7
)

# Output the response
print("\n--- Response ---")
print(completion.choices[0].message.content)
