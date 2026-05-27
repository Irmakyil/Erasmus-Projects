# Name: Irmak Yılmaz
# Student Number: E-379
# Steganography Tool (Text-in-Image using LSB)

from PIL import Image
import os

def text_to_bin(text):
    """Converts a text string to a binary string."""
    return ''.join(format(ord(c), '08b') for c in text)

def bin_to_text(binary_string):
    """Converts a binary string back to text."""
    message = ""
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        if byte:
            message += chr(int(byte, 2))
    return message

def hide_message(image_path, secret_message, output_path):
    """Hides a secret message inside an image using LSB steganography."""
    image = Image.open(image_path)
    # Convert image to standard RGB mode just in case
    encoded_image = image.convert('RGB')
    width, height = encoded_image.size
    
    # We add a specific delimiter to know where the message ends during extraction
    secret_message += "#####"
    binary_msg = text_to_bin(secret_message)
    msg_len = len(binary_msg)
    
    if msg_len > width * height * 3:
        raise ValueError("Error: The message is too long to be hidden in this image.")
    
    data_index = 0
    
    for y in range(height):
        for x in range(width):
            pixel = list(encoded_image.getpixel((x, y)))
            
            # Modify the Least Significant Bit (LSB) of Red, Green, and Blue channels
            for n in range(3): 
                if data_index < msg_len:
                    # Clear the LSB and set it to our message bit
                    pixel[n] = pixel[n] & ~1 | int(binary_msg[data_index])
                    data_index += 1
                    
            encoded_image.putpixel((x, y), tuple(pixel))
            
            if data_index >= msg_len:
                # MUST save as PNG to prevent lossy compression from destroying the LSBs
                encoded_image.save(output_path, "PNG")
                print(f"[SUCCESS] Message successfully hidden in '{output_path}'")
                return

def extract_message(image_path):
    """Extracts a hidden message from an image."""
    image = Image.open(image_path)
    image = image.convert('RGB')
    width, height = image.size
    binary_msg = ""
    
    for y in range(height):
        for x in range(width):
            pixel = list(image.getpixel((x, y)))
            
            # Read the LSB of Red, Green, and Blue channels
            for n in range(3):
                binary_msg += str(pixel[n] & 1)
                
    extracted_text = bin_to_text(binary_msg)
    
    # Cut off the string at the delimiter
    if "#####" in extracted_text:
        return extracted_text.split("#####")[0]
    else:
        return "[ERROR] No hidden message found or image is corrupted."

def main():
    print("=== Steganography Tool (LSB Method) ===")
    
    original_img = "istanbul-view.png"
    encoded_img = "encoded_istanbul.png"
    
    # Check if the user has put the image in the directory
    if not os.path.exists(original_img):
        print(f"[ERROR] Please make sure '{original_img}' is in the same folder as this script!")
        return
        
    secret_text = "Erasmus Secret Data: Greetings from an Istanbul in Poland. The server password is 'Galata2026!'"
    
    # 1. Hide the message
    print(f"\nHiding message: '{secret_text}'")
    hide_message(original_img, secret_text, encoded_img)
    
    # 2. Extract the message
    print("\nExtracting message from the encoded image...")
    revealed_text = extract_message(encoded_img)
    print(f"[REVEALED MESSAGE] -> {revealed_text}")

if __name__ == "__main__":
    main()