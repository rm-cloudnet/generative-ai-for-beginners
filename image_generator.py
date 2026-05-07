import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables
load_dotenv()
hf_token = os.getenv("HUGGING_FACE_API_KEY")

# Initialize the client
client = InferenceClient(token=hf_token)

# Choose a state-of-the-art image model
# FLUX.1-schnell is very fast and great for the free tier
model_id = "black-forest-labs/FLUX.1-schnell"

prompt = input("Describe the image you want to create: ")

print(f"\nGenerating image using {model_id}...")

# Generate the image
image = client.text_to_image(prompt, model=model_id)


# Save the image to your VM
base_name = input("Save the file as: ")

# Ensure file name with .png
if not base_name.lower().endswith(".png"):
    file_name = f"{base_name}.png"
else:
    file_name = base_name
image.save(file_name)

print(f"Success! Your image has been saved as {file_name}")
