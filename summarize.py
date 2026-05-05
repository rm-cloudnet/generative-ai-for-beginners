from tokenizers import Tokenizer

# Initialize the lightweight tokenizer
tokenizer = Tokenizer.from_pretrained("gpt2")

# Define the text from the notebook
text = """
Jupiter is the fifth planet from the Sun and the 
largest in the Solar System. It is a gas giant with 
a mass one-thousandth that of the Sun, but two-and-a-half 
times that of all the other planets in the Solar System combined. 
"""

# Combine into the prompt template
prompt = f"""
Summarize the content you are provided with for a second-grade student.
{text}
"""

# Tokenize the prompt to see how the model reads it
output = tokenizer.encode(prompt)

print("Prompt Token IDs:")
print(output.ids)
print(f"\nTotal prompt tokens: {len(output.ids)}")
