"""
Name: Irmak YILMAZ
Student ID: E-379
Language: Python 3
"""

import re

def preprocess_text(text):
    """
    Convert text to lowercase, remove spaces,
    and validate that it contains ONLY a-z letters.
    """

    # Remove spaces and convert to lowercase
    text = text.lower().replace(" ", "")

    # Ensure only Latin letters a-z are used
    if not re.fullmatch(r"[a-z]+", text):
        print("Error: Only Latin letters (a-z) are allowed.")
        return None

    return text


def encrypt(text, key):
    """
    Encrypt text using Caesar cipher formula:
    (m - 97 + k) mod 26 + 97
    """
    result = ""

    for char in text:
        m = ord(char)
        encrypted = (m - 97 + key) % 26 + 97
        result += chr(encrypted)

    return result


def decrypt(text, key):
    """
    Decrypt text using Caesar cipher formula:
    (m - 97 - k) mod 26 + 97
    """
    result = ""

    for char in text:
        m = ord(char)
        decrypted = (m - 97 - key) % 26 + 97
        result += chr(decrypted)

    return result


def main():
    print("--- Caesar Cipher Program ---")

    # Input text
    text = input("Enter text: ")

    # Preprocess and validate
    processed_text = preprocess_text(text)
    if processed_text is None:
        return

    # Input key
    try:
        key = int(input("Enter key (positive natural number): "))

        if key <= 0:
            print("Error: Key must be a positive natural number.")
            return

    except ValueError:
        print("Error: Key must be an integer.")
        return

    # Action selection
    choice = input("Choose action (1: Encrypt, 2: Decrypt): ")

    # Process
    if choice == '1':
        result = encrypt(processed_text, key)
        print("\nEncrypted text:", result)

    elif choice == '2':
        result = decrypt(processed_text, key)
        print("\nDecrypted text:", result)

    else:
        print("Error: Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()