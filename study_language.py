import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from .env file
load_dotenv()

# Get the Hugging Face API key stored in the environment variable
hf_token = os.getenv("HUGGING_FACE_API_KEY")

# Configure the Hugging Face Inference Client
client = InferenceClient(token=hf_token)

# Use the highly-capable Zephyr instruction model
model_id = "HuggingFaceH4/zephyr-7b-beta"

# Get a question on the Python language from the user
question = input("Ask your questions on python language to your study buddy: ")

# Prepare the prompt with instructions and the user's question
prompt = f"""
You are an expert on the python language.

Whenever certain questions are asked, you need to provide response in below format.

- Concept
- Example code showing the concept implementation
- explanation of the example and how the concept is done for the user to understand better.

Provide answer for the question: {question}
"""

messages = [{"role": "user", "content": prompt}]

# Make the request to the conversational API
completion = client.chat_completion(
    model=model_id,
    messages=messages,
    max_tokens=250,
    temperature=0.7
)

# Print the generated response
print(completion.choices[0].message.content)
