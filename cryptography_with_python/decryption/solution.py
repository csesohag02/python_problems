"""
Created on Sat Nov  9 23:55:02 2024
@author: csesohag02
"""


# list of the characters
characters = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
length = len(characters)


# decrypt function
def decrypt(p_text, p_shift):
    """
    decrypt(text, shift) -> decrypted text
    Take the encrypted text and shift number; return the decrypted text
    """
    decrypt_text = ""
    for char in p_text:
        position = characters.index(char)
        new_position = position - p_shift
        if new_position < 0:
            new_position = new_position + length
        new_char = characters[new_position]
        decrypt_text += new_char
    return decrypt_text


encrypt_message = input("Enter the encrypted message: ")
shift = int(input("Enter the shift number: "))
message = decrypt(encrypt_message, shift)
print(f"Your decrypted message: {message}")
