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

# Get user inputs for recipes
no_recipes = input("No of recipes (for example, 5): ")
ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")
filter_input = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

# 1. Interpolate the inputs into the first prompt
prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter_input}."
messages = [{"role": "user", "content": prompt}]

print("\nGenerating recipes...\n")

# Make the request to the conversational API
completion = client.chat_completion(
    model=model_id,
    messages=messages,
    max_tokens=600,
    temperature=0.1
)

recipes_result = completion.choices[0].message.content
print("Recipes:")
print(recipes_result)

# 2. Prepare the prompt for the shopping list
prompt_shopping = "Produce a shopping list, and please don't include ingredients that I already have at home: "
new_prompt = f"Given ingredients at home {ingredients} and these generated recipes: {recipes_result}, {prompt_shopping}"
messages_shopping = [{"role": "user", "content": new_prompt}]

print("\nGenerating shopping list...\n")

completion_shopping = client.chat_completion(
    model=model_id,
    messages=messages_shopping,
    max_tokens=600,
    temperature=0
)

# Print the final shopping list response
print("====== Shopping list ======= \n")
print(completion_shopping.choices[0].message.content)
