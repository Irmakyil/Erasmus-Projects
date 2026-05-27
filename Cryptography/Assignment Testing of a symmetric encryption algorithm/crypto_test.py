import os
import time
import psutil
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

def create_dummy_file(filename, size_mb):
    """Creates a file containing random data of the specified size (in MB)."""
    print(f"Creating [{filename}] ({size_mb} MB)...")
    with open(filename, 'wb') as f:
        f.write(os.urandom(size_mb * 1024 * 1024))

def measure_performance(func, *args):
    """Measures the execution time, CPU usage, and RAM consumption of a function."""
    process = psutil.Process(os.getpid())
    
    # Initial values
    start_time = time.time()
    start_ram = process.memory_info().rss / (1024 * 1024) # in MB
    psutil.cpu_percent(interval=None) # Initialize CPU measurement
    
    # Execute the function (encryption/decryption)
    result = func(*args)
    
    # Final values
    end_time = time.time()
    cpu_usage = psutil.cpu_percent(interval=None)
    end_ram = process.memory_info().rss / (1024 * 1024)
    
    execution_time = end_time - start_time
    ram_used = max(0, end_ram - start_ram)
    
    return result, execution_time, cpu_usage, ram_used

def encrypt_data(data, key, nonce):
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None)
    encryptor = cipher.encryptor()
    return encryptor.update(data)

def decrypt_data(data, key, nonce):
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None)
    decryptor = cipher.decryptor()
    return decryptor.update(data)

def main():
    file_sizes = [1, 10, 100] # File sizes in MB
    
    # Generating a 256-bit (32 byte) key and 16 byte nonce for ChaCha20
    key = os.urandom(32)
    nonce = os.urandom(16)
    
    print("=== Starting ChaCha20 Performance Test ===\n")
    
    for size in file_sizes:
        filename = f"dataset_{size}MB.txt"
        create_dummy_file(filename, size)
        
        with open(filename, 'rb') as f:
            plaintext = f.read()
            
        print(f"\n--- Testing {size} MB Dataset ---")
        
        # 1. Encryption Test
        ciphertext, enc_time, enc_cpu, enc_ram = measure_performance(encrypt_data, plaintext, key, nonce)
        print(f"ENCRYPTION -> Time: {enc_time:.4f} sec | CPU: {enc_cpu:.1f}% | RAM spike: {enc_ram:.2f} MB")
        
        # 2. Decryption Test
        decrypted_data, dec_time, dec_cpu, dec_ram = measure_performance(decrypt_data, ciphertext, key, nonce)
        print(f"DECRYPTION -> Time: {dec_time:.4f} sec | CPU: {dec_cpu:.1f}% | RAM spike: {dec_ram:.2f} MB")
        
        # 3. Verification
        if plaintext == decrypted_data:
            print("Status: Success! Decrypted data matches original plaintext.")
        else:
            print("Status: FAILED! Data does not match.")
            
        # Clean up dummy files
        os.remove(filename)

if __name__ == "__main__":
    main()