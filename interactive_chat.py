import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from .env file
load_dotenv()

# Get your Hugging Face API key
hf_token = os.getenv("HUGGING_FACE_API_KEY")

# Initialize the lightweight inference client
client = InferenceClient(token=hf_token)

# Use the highly capable conversational model
model_id = "HuggingFaceH4/zephyr-7b-beta"

# Initialize conversation history with a system prompt
messages = [
    {"role": "system", "content": "You are a concise, helpful assistant. Answer the user directly without conversational tags."}
]

print("Chatbot initialized! Type 'exit' or 'quit' to end the conversation.\n")

while True:
    user_query = input("Ask your question: ")
    
    if user_query.lower() in ['exit', 'quit']:
        print("\nExiting chat. Goodbye!")
        break

# Create a fresh message payload for each turn to avoid history contamination
    messages = [
        {"role": "system", "content": "You are a concise, helpful assistant."},
        {"role": "user", "content": user_query}
    ]

    try:
        # Generate the chat completion using the remote API
        completion = client.chat_completion(
            model=model_id,
            messages=messages,
            max_tokens=300,
            temperature=0.7,
            stop=["[/ASSIST]", "[USER]"]
        )

        assistant_response = completion.choices[0].message.content

        # Output the response
        print("\n--- Response ---")
        print(assistant_response)
        print("-" * 18 + "\n")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
