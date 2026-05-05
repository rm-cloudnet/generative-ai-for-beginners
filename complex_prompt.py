from transformers import AutoTokenizer

# 1. Load a tokenizer that supports chat templates (e.g., Phi-3 or similar instruction models)
model_id = "microsoft/Phi-3-mini-4k-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id)

# 2. Define the multi-turn conversation messages
messages = [
    {"role": "system", "content": "You are a sarcastic assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "Who do you think won? The Los Angeles Dodgers of course."},
    {"role": "user", "content": "Where was it played?"}
]

# 3. Format the chat template
# tokenize=False keeps this lightweight and doesn't require PyTorch dependencies
formatted_prompt = tokenizer.apply_chat_template(
    messages, 
    tokenize=False, 
    add_generation_prompt=True
)

print("Formatted Prompt Output:")
print(formatted_prompt)
