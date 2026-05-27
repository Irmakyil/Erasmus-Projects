"""
Name: Irmak YILMAZ
Student ID: E-379
Language: Python 3
"""

def to_binary_string(text):
    """
    Converts a string into its 8-bit binary representation.
    """
    return ' '.join(format(ord(char), '08b') for char in text)


def extend_key(message, key):
    """
    Repeats the key so that its length matches the message length.
    """
    return ''.join(key[i % len(key)] for i in range(len(message)))


def xor_encrypt(message, key):
    """
    Encrypts the message using XOR and maps result to printable ASCII (32–126).
    """
    extended_key = extend_key(message, key)
    result_chars = []

    for i in range(len(message)):
        m = ord(message[i])
        k = ord(extended_key[i])

        # XOR operation
        xor_val = m ^ k

        # Map result to printable ASCII range (32–126)
        printable_val = (xor_val % 95) + 32

        result_chars.append(chr(printable_val))

    return ''.join(result_chars)


def xor_decrypt(ciphertext, key):
    """
    Decrypts the message using XOR (reverse mapping from printable ASCII).
    """
    extended_key = extend_key(ciphertext, key)
    result_chars = []

    for i in range(len(ciphertext)):
        c = ord(ciphertext[i])
        k = ord(extended_key[i])

        # Reverse mapping from printable ASCII
        xor_val = (c - 32)

        # XOR to recover original character
        original_val = xor_val ^ k

        result_chars.append(chr(original_val))

    return ''.join(result_chars)


def hex_to_string(hex_input):
    """
    Converts hex string back to normal string.
    """
    bytes_object = bytes.fromhex(hex_input)
    return bytes_object.decode('utf-8', errors='ignore')


def main():
    print("--- XOR Cipher Program ---")

    message = input("Enter the message: ")
    key = input("Enter the key: ")

    if not message or not key:
        print("Error: Message and key cannot be empty.")
        return

    print("\nSelect an option:")
    print("1. Encrypt message")
    print("2. Decrypt message")
    choice = input("Choice (1/2): ")

    if choice == '1':
        print("\n--- Encryption ---")

        print("\nMessage (Binary):")
        print(to_binary_string(message))

        print("\nKey (Binary):")
        print(to_binary_string(extend_key(message, key)))

        encrypted = xor_encrypt(message, key)

        print("\nCiphertext (Printable ASCII):")
        print(encrypted)

        print("\nCiphertext (Hex):")
        print(encrypted.encode().hex())

    elif choice == '2':
        print("\n--- Decryption ---")

        print("Input type:")
        print("1. Printable ASCII")
        print("2. Hex format")

        input_type = input("Choice (1/2): ")

        if input_type == '2':
            message = hex_to_string(message)

        decrypted = xor_decrypt(message, key)

        print("\nDecrypted Message:")
        print(decrypted)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()