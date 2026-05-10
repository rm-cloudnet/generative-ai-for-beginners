import os
import re
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from promptflow.core import tool

load_dotenv()

@tool
def classify_intent(question: str):
    client = InferenceClient(token=os.getenv("HUGGING_FACE_API_KEY"))
    model_id = "HuggingFaceH4/zephyr-7b-beta"
    
    messages = [
        {"role": "system", "content": "Extract task. Format: 'GROCERY: item' or 'TODO: item'. Only output the format."},
        {"role": "user", "content": question}
    ]

    response = client.chat_completion(
        messages=messages,
        model=model_id,
        max_tokens=20,
        temperature=0.1
    )
    
    raw_result = response.choices[0].message.content.strip()
    
    # 1. Remove bracketed tags like [ASSISTANT]
    clean_result = re.sub(r'\[.*?\]', '', raw_result).strip()
    
    # 2. If it already has a category, just return it
    if ":" in clean_result:
        # Check if it's doubled like "GROCERY: GROCERY: eggs"
        parts = clean_result.split(":")
        if len(parts) > 2:
             clean_result = f"{parts[-2].strip()}: {parts[-1].strip()}"
        return clean_result

    # 3. If it's just the item name, assume GROCERY (fallback)
    return f"GROCERY: {clean_result}"
