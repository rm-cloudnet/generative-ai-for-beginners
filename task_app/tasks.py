import os
from promptflow.core import tool

@tool
def manage_tasks(intent_output: str):
    if ":" not in intent_output:
        return f"Format Error: {intent_output}"

    # Split and take only the last two parts to handle double colons
    parts = intent_output.split(":")
    category = parts[-2].strip().upper()
    item = parts[-1].strip()

    if not item:
        return "Error: No item found."

    # Force a clean filename
    filename = "groceries.txt" if "GROCERY" in category else "todo.txt"
    
    with open(filename, "a") as f:
        f.write(f"- {item}\n")
    
    return f"Saved '{item}' to {filename}"

# Quick snippet to clean your text files if they get messy
def clean_list(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    clean_lines = [l for l in lines if l.strip().startswith("-")]
    with open(filename, "w") as f:
        f.writelines(clean_lines)
