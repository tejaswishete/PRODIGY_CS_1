#Implementation of Caesar Cipher Algorithm

def caesar_cipher(text, shift):
    """Encrypt or decrypt a text using Caesar Cipher with a given shift."""
    result = []
    for char in text:

        if char.isalpha():  # Check if the character is an alphabet
            # Determine if the character is uppercase or lowercase

            base = ord('A') if char.isupper() else ord('a')
            # Compute the shifted character

            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))

        else:
            # Non-alphabetic characters are added unchanged
            result.append(char)
    return ''.join(result)


def main():
    print("Caesar Cipher Program")
    
    # Input message
    message = input("Enter the message: ")
    
    # Input shift value
    shift = int(input("Enter the shift value: "))
    
    # Encrypt the message
    encrypted_message = caesar_cipher(message, shift)
    print(f"Encrypted message: {encrypted_message}")
    
    # Decrypt the message
    decrypted_message = caesar_cipher(encrypted_message, -shift)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()

