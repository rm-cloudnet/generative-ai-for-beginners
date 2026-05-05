from dotenv import load_dotenv
import os
from transformers import AutoTokenizer

# Load environment variables from the .env file
load_dotenv()

# Access the Hugging Face API Key
hf_token = os.getenv("HUGGING_FACE_API_KEY")
print(f"Loaded Hugging Face Key successfully! Key starts with: {hf_token[:7] if hf_token else 'None'}")

# Initialize the Hugging Face Tokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Define the text you want to tokenize
#text = """
#Jupiter is the fifth planet from the Sun and the 
#largest in the Solar System. It is a gas giant with 
#a mass one-thousandth that of the Sun, but two-and-a-half 
#times that of all the other planets in the Solar System combined. 
#Jupiter is one of the brightest objects visible to the naked eye 
#in the night sky, and has been known to ancient civilizations since 
#before recorded history. It is named after the Roman god Jupiter.
#When viewed from Earth, Jupiter can be bright enough for its reflected 
#light to cast visible shadows, and is on average the third-brightest 
#natural object in the night sky after the Moon and Venus.
#"""

text = """
A computer network or data network is a telecommunications network 
that allows computers to exchange data. Networked computing devices 
pass data to each other in the form of packets across connections established 
using either cable or wireless media
"""





# Encode the text into token IDs
tokens = tokenizer.encode(text)

print("\nToken IDs:")
print(tokens)

# Decode the tokens back into text
decoded_text = tokenizer.decode(tokens)

print("\nDecoded text:")
print(decoded_text)
