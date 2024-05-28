import random
import string

def create_password(length, include_letters, include_numbers, include_symbols):
    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        return "No character types selected. Please try again."

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password

def start():
    print("Welcome to the Password Generator!")

    length = int(input("Enter the desired length of the password: "))
    include_letters = input("Include letters (y/n)? ").lower() == 'y'
    include_numbers = input("Include numbers (y/n)? ").lower() == 'y'
    include_symbols = input("Include symbols (y/n)? ").lower() == 'y'

    password = create_password(length, include_letters, include_numbers, include_symbols)

    print("Generated Password:", password)

if __name__ == "__main__":
    start()
