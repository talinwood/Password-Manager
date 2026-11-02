import os 
import hashlib
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag

salt_size = 16
nonce_size = 12
key_size = 32
iterations = 600000

def derive_key(master_password, salt):
    return hashlib.pbkdf2_hmac("sha256", master_password.encode(), salt, iterations, key_size)


def encrypt_vault(plaintext, master_password):
    salt = os.urandom(salt_size)
    nonce = os.urandom(nonce_size)

    # master password -> key
    key = derive_key(master_password, salt)

    #encrypt vault
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    #converting bytes into text so that they can be saved in JSON
    salt_text = base64.b64encode(salt).decode()
    nonce_text = base64.b64encode(nonce).decode()
    ciphertext_text = base64.b64encode(ciphertext).decode()


    return { "salt": salt_text, "nonce": nonce_text, "ciphertext": ciphertext_text}


def decrypt_vault(encrypted, master_password):

    #converting the text back into bytes
    salt = base64.b64decode(encrypted["salt"])
    nonce = base64.b64decode(encrypted["nonce"])
    ciphertext = base64.b64decode(encrypted["ciphertext"])

    # master password + saved salt = same key
    key = derive_key(master_password, salt)

    #decrypt the vault
    aesgcm = AESGCM(key)
    try:
        plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    except InvalidTag:
        raise ValueError("Wrong master password or vault file was modified.")

    return plaintext


if __name__ == "__main__":
    import json

    entries = [
        {"site": "github.com", "username": "oozername", "password": "pass1624"}
    ]

    # entry turned into bytes
    plaintext = json.dumps(entries).encode()

    #encrypt
    encrypted = encrypt_vault(plaintext, "testpass")
    print("Encrypted: ", encrypted)

    #decrypt and turn back into a list
    decrypted = decrypt_vault(encrypted, "testpass")
    print("Decrypted: ", json.loads(decrypted))


    #wrong password
    try:
        decrypt_vault(encrypted, "wrongpass")
    except ValueError as e:
        print("Wrong password: ", e)