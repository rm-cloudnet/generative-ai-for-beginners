import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from .env file
load_dotenv()

# Get the Hugging Face API key stored in the environment variable
hf_token = os.getenv("HUGGING_FACE_API_KEY")

# Configure the Hugging Face Inference Client
client = InferenceClient(token=hf_token)

# Use a free, highly-capable model available via the API
model_id = "HuggingFaceH4/zephyr-7b-beta"

# Add your completion prompt
messages = [{"role": "user", "content": "Once upon a time there was a"}]

# Make completion request to the serverless API
completion = client.chat_completion(
    model=model_id,
    messages=messages,
    max_tokens=100,
    temperature=0.7
)

# Print the generated response
print(completion)
