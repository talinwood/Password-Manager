import json
import os


# Save encrypted vault data to a file
def save_vault(filepath, vault_data):

    temp_path = filepath + ".tmp"

    try:
        with open(temp_path, "w", encoding="utf-8") as file:
            json.dump(vault_data, file)

        os.replace(temp_path, filepath)

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


# Load encrypted vault data from a file
def load_vault(filepath):

    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)
