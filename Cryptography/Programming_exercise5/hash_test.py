import hashlib
import time
import os
import math

def get_binary_string(byte_data):
    """Converts bytes to a continuous binary string (0s and 1s)"""
    return ''.join(format(b, '08b') for b in byte_data)

def calculate_entropy(binary_string):
    """Calculates the Shannon entropy and the distribution of 0s and 1s"""
    zeros = binary_string.count('0')
    ones = binary_string.count('1')
    total_bits = len(binary_string)
    
    p0 = zeros / total_bits
    p1 = ones / total_bits
    
    entropy = 0
    if p0 > 0: entropy -= p0 * math.log2(p0)
    if p1 > 0: entropy -= p1 * math.log2(p1)
        
    return entropy, zeros, ones

def test_determinism():
    print("--- 1. Determinism Test ---")
    message = b"ErasmusCryptographyProject"
    
    hash1 = hashlib.sha256(message).hexdigest()
    hash2 = hashlib.sha256(message).hexdigest()
    
    print(f"Message   : {message.decode()}")
    print(f"Hash 1    : {hash1}")
    print(f"Hash 2    : {hash2}")
    if hash1 == hash2:
        print("Result    : SUCCESS (Both hashes are strictly identical)\n")
    else:
        print("Result    : FAILED\n")

def test_avalanche_effect():
    print("--- 2. Avalanche Effect Test ---")
    # "Data" and "data" differ by exactly 1 bit in ASCII (D is 01000100, d is 01100100)
    msg1 = b"Data"
    msg2 = b"data"
    
    hash1_bytes = hashlib.sha256(msg1).digest()
    hash2_bytes = hashlib.sha256(msg2).digest()
    
    bin1 = get_binary_string(hash1_bytes)
    bin2 = get_binary_string(hash2_bytes)
    
    # Calculate Hamming distance (number of differing bits)
    changed_bits = sum(1 for bit1, bit2 in zip(bin1, bin2) if bit1 != bit2)
    total_bits = 256
    change_percentage = (changed_bits / total_bits) * 100
    
    print(f"Input 1   : '{msg1.decode()}'")
    print(f"Input 2   : '{msg2.decode()}' (1 bit changed)")
    print(f"Bits flipped in Hash : {changed_bits} out of {total_bits}")
    print(f"Avalanche Effect     : {change_percentage:.2f}%\n")

def test_performance():
    print("--- 3. Performance Test ---")
    sizes = [1, 100, 1024] # 1 KB, 100 KB, 1 MB (1024 KB)
    
    for size in sizes:
        data = os.urandom(size * 1024)
        
        start_time = time.time()
        hashlib.sha256(data).digest()
        end_time = time.time()
        
        exec_time = end_time - start_time
        unit = "KB" if size < 1024 else "MB"
        display_size = size if size < 1024 else size // 1024
        
        print(f"Hashing {display_size} {unit} file took: {exec_time:.6f} seconds")
    print()

def test_bit_level_analysis():
    print("--- 4. Bit-Level Analysis (Entropy & Distribution) ---")
    # Generate a hash for a sample text
    msg = b"A completely random string to test the entropy of SHA-256 output."
    hash_bytes = hashlib.sha256(msg).digest()
    binary_str = get_binary_string(hash_bytes)
    
    entropy, zeros, ones = calculate_entropy(binary_str)
    
    print(f"Total Bits Evaluated : {len(binary_str)}")
    print(f"Number of 0s         : {zeros}")
    print(f"Number of 1s         : {ones}")
    print(f"Ideal Entropy        : 1.0 (Perfect randomness)")
    print(f"Calculated Entropy   : {entropy:.6f}\n")

def main():
    print("=== Cryptographic Hash Function Tests (SHA-256) ===\n")
    test_determinism()
    test_avalanche_effect()
    test_performance()
    test_bit_level_analysis()

if __name__ == "__main__":
    main()