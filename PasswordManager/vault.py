import json
from encryption import encrypt_vault, decrypt_vault
from storage import save_vault, load_vault
from password_entry import PasswordEntry


# encrypts all the entries and saves to vault file
def save_entries(filepath, entries, master_pass):
    # turning each entry into dictionary
    data = []
    for entry in entries:
        data.append(entry.to_dict())

    # turning list into bytes and encrypting it
    plaintext = json.dumps(data).encode()
    encrypted = encrypt_vault(plaintext, master_pass)

    #saving ONLY the encrypted data
    save_vault(filepath, encrypted)


# loads the vault file, decrypts it, and returns the entries
# raises ValueError if password was worong or file was modified
def load_entries(filepath, master_pass):

    # loading and decrypting file
    encrypted = load_vault(filepath)
    plaintext = decrypt_vault(encrypted, master_pass)


    # turning the bytes back into entries
    data = json.loads(plaintext)
    entries = []
    for item in data:
        entries.append(PasswordEntry.from_dict(item))

    return entries


if __name__ == "__main__":
    import os 

    test_file = "test_vault.json"

    # just making some test entries and saving
    entries = [
        PasswordEntry("github.com", "oozername", "pass1624"),
        PasswordEntry("reddit.com", "Turing", "Bombe"),
        PasswordEntry("canvas.com", "Stooodent", "Homework!")
    ]
    save_entries(test_file, entries, "testpass")

    # showing whats actually in the file, should be no readable passwords (hopefully xD)
    with open(test_file, "r") as f:
        print("File contents: ", f.read())


    # loading with the CORRECT pass
    loaded = load_entries(test_file, "testpass")
    for entry in loaded:
        print("Loaded: ", entry.get_website(), entry.get_username(), entry.get_password())


    # loading with the INCORRECT pass (should fail)
    try:
        load_entries(test_file, "wrongpass")
    except ValueError as e:
        print("Wrong password: ", e)


    # deleting test file
    os.remove(test_file)
