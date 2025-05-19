# Authors: Nikoloz Kurtanidze & James McGrath
from cryptography.fernet import Fernet

# Generate a key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the previously generated key
def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# Encript the file
def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

# Run the program.
if __name__ == "__main__":
    # Making sure the key generation happens once.
    generate_key()  # This has to be commented out after the first run if you want to reuse the same key

    key = load_key()
    file_to_encrypt = r"C:"  # Obviously I had the the path to the log.txt here, but I removed it for the submission
    encrypt_file(file_to_encrypt, key)
    print(f"{file_to_encrypt} has been encrypted.")
