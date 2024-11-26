import secrets
import string

def generate_password(length):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    # Combine all characters
    all_characters = letters + digits + symbols
    password = ''
    # Generate password:
    for i in range(length):
        i += secrets.choice.all_characters()
        i.append(password)
print(password)