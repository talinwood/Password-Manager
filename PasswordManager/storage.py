import json
import os

#Save the vault data to a JSON file.
def save_vault(filepath, vault_data):

    # Create a temporary file path
    temp_path = filepath+ ".tmp"

    # Write the vault data to the temporary file
    with open(temp_path, 'w') as file:
        json.dump(vault_data, file)

    # Atomically replace the original file with the temp file
    os.replace(temp_path, filepath)

# Load the vault data from a JSON file.
def load_vault(filepath):

    # Check if the file exists
    with open(filepath, 'r') as file:
        return json.load(file)