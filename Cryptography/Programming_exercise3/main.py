"""
Name: Irmak YILMAZ
Student ID: E-379
Language: Python 3

--- INSTRUCTIONS FOR EVALUATOR ---
1. Please create a file named 'input.txt' in the same directory using the 'New File' button in OnlineGDB.
2. Write some text inside 'input.txt' and save it.
3. Run this program and provide 'input.txt' as the input path.
4. The result will be generated as 'output.txt' in the sidebar.
----------------------------------
"""

import os

def get_permutation_dicts(permutation):
    """Create encryption and decryption mappings."""
    encrypt_map = {}
    decrypt_map = {}

    for i, p in enumerate(permutation):
        encrypt_map[i] = p - 1
        decrypt_map[p - 1] = i

    return encrypt_map, decrypt_map


def apply_permutation(text, n, mapping):
    """Apply permutation block by block."""
    result = ""

    for i in range(0, len(text), n):
        block = text[i:i + n]

        if len(block) < n:
            result += block
            continue

        new_block = [""] * n
        for old_pos, new_pos in mapping.items():
            new_block[new_pos] = block[old_pos]

        result += "".join(new_block)

    return result


def encrypt(text, n, enc_map):
    """Encrypt text with padding tracking."""

    padding_len = 0

    if len(text) % n != 0:
        padding_len = n - (len(text) % n)
        text += text[:padding_len]

    encrypted = apply_permutation(text, n, enc_map)

    # Store padding length at the beginning
    return str(padding_len) + "|" + encrypted


def decrypt(text, n, dec_map):
    """Decrypt text and remove padding."""

    try:
        padding_len_str, actual_text = text.split("|", 1)
        padding_len = int(padding_len_str)
    except:
        print("Error: Invalid encrypted format.")
        return ""

    decrypted = apply_permutation(actual_text, n, dec_map)

    # Remove padding
    if padding_len > 0:
        decrypted = decrypted[:-padding_len]

    return decrypted


def process_file(input_path, output_path, n, permutation, action):
    """Handle file operations."""

    if not os.path.exists(input_path):
        print("Error: Input file not found.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        message = f.read()

    enc_map, dec_map = get_permutation_dicts(permutation)

    if action == '1':
        result = encrypt(message, n, enc_map)
        status = "Encryption"
    elif action == '2':
        result = decrypt(message, n, dec_map)
        status = "Decryption"
    else:
        print("Invalid action.")
        return

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"\nSuccess! {status} completed.")
    print(f"Output saved to: {output_path}")


def main():
    print("--- Block Permutation Cipher ---")

    try:
        input_file = input("Enter input file path: ")
        output_file = input("Enter output file path: ")

        n = int(input("Enter block size (n): "))

        perm_input = input(f"Enter permutation (1 to {n}): ")
        permutation = [int(x) for x in perm_input.split()]

        if len(permutation) != n:
            print("Error: Invalid permutation length.")
            return

        if sorted(permutation) != list(range(1, n + 1)):
            print("Error: Invalid permutation values.")
            return

        action = input("Encryption (1) or Decryption (2): ")

        process_file(input_file, output_file, n, permutation, action)

    except ValueError:
        print("Error: Invalid input.")


if __name__ == "__main__":
    main()