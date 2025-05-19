# Authors: Nikoloz Kurtanidze & James McGrath

from cryptography.fernet import Fernet

# Load the existing key
def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# Decrypt the file
def decrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        encrypted = file.read()
    try:
        decrypted = fernet.decrypt(encrypted)
        with open(filename, "wb") as decrypted_file:
            decrypted_file.write(decrypted)
        print(f"{filename} has been decrypted.")
    except Exception as e:
        print(f"Error: Could not decrypt {filename}. Reason: {e}")

# execution
if __name__ == "__main__":
    key = load_key()
    file_to_decrypt = ""  #  Obviously I had the the path to the log.txt here, but I removed it for the submission
    decrypt_file(file_to_decrypt, key)
