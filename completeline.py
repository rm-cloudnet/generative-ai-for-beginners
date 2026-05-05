from transformers import pipeline

# Load a text generation pipeline using GPT-2
generator = pipeline("text-generation", model="gpt2")

# Set the prompt text
prompt = "oh say can you see"

# Generate text completion
result = generator(prompt, max_length=30, num_return_sequences=1)

print("Generated Completion:")
print(result[0]['generated_text'])
