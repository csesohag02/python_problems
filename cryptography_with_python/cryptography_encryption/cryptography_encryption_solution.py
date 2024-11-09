"""
Created on Sat Nov  9 23:21:32 2024
@author: csesohag02
"""


# list of the characters
characters = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
length = len(characters)


# encrypt function
def encrypt(p_text, p_shift):
    """
    encrypt(text, shift) -> encypted_text
    Take the text and shift number; return the encrypted text
    """
    encrypt_text = ""
    for char in p_text:
        position = characters.index(char)
        new_position = position + p_shift
        if new_position > length-1:
            new_position = new_position - length
        new_char = characters[new_position]
        encrypt_text += new_char
    return encrypt_text


message = input("Enter your message: ")
shift = int(input("Enter the shift number: "))
encrypt_message = encrypt(message, shift)
print(f"Your encrypted message : {encrypt_message}")
