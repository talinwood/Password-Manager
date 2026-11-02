import os 
import hashlib
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag

salt_size = 16 # random per save so same pass never makes same key
nonce_size = 12 
key_size = 32 # 32 bytes is 256 bits
iterations = 600000 # many iterations so its slow to mitigate brute force attack


# turning the master pass into a 256 bit key using PBKDF2-HMAC-SHA256
# same password with the same salt always gives same key (unlocking)
def derive_key(master_pass, salt):
    return hashlib.pbkdf2_hmac("sha256", master_pass.encode(), salt, iterations, key_size)


# encrypts the vault and returns everything thats needed to decrypt it later
# master pass and key are NEVER stored, only the salt, nonce and the ciphertext are
def encrypt_vault(plaintext, master_pass):
    # new random salt and nonce every save to prevent attacks
    salt = os.urandom(salt_size)
    nonce = os.urandom(nonce_size)

    # master password -> key
    key = derive_key(master_pass, salt)

    # encrypt vault and the GCM also adds the 16 byte tag to end of ciphertext
    # (tag is what lets us detect wrong pass or modified file later)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    # salt and nonce arent secret but they are random so they have to be saved to decrypt later
    # urandom and AESGCM give actual bytes which cant be stored in JSON
    # b64encode makes them safe text chars then decode turns that into a normal string and not b
    salt_text = base64.b64encode(salt).decode()
    nonce_text = base64.b64encode(nonce).decode()
    ciphertext_text = base64.b64encode(ciphertext).decode()


    return { "salt": salt_text, "nonce": nonce_text, "ciphertext": ciphertext_text}


# decrypts the vault with the saved nonce and salt
def decrypt_vault(encrypted, master_pass):

    # converting the text back into bytes
    salt = base64.b64decode(encrypted["salt"])
    nonce = base64.b64decode(encrypted["nonce"])
    ciphertext = base64.b64decode(encrypted["ciphertext"])

    # master password + saved salt = same key (if pass is right)
    key = derive_key(master_pass, salt)

    # decrypt the vault, GCM recomputes the tag and compares it to the previously saved one
    # if no match bc of wrong pass or changed data then raises invalidTag
    aesgcm = AESGCM(key)
    try:
        plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    except InvalidTag:
        raise ValueError("Wrong master password or vault file was modified.")

    return plaintext


# test
if __name__ == "__main__":
    import json

    entries = [
        {"website": "github.com", "username": "oozername", "password": "pass1624"}
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