"""
Created on Sun Nov 10 01:37:32 2024
@author: csesohag02
"""


#import crypto module
import crypto


print("************** MAIN MENU **************")
print("E -> Encrypt Message")
print("D -> Decrypt Message")
print("S -> Stop")
print("---------------------------------------")


while True:
    user_action = input("\nWhat you want to do?(choose option from the MAIN MENU): ")
    
    if user_action == 'S':
        print("See you next time!")
        break
    
    elif user_action in ('E', 'D'):
        message = input("Enter the message: ")
        shift = int(input("Enter the shift number: "))
        if user_action == 'E':
            encrypt_message = crypto.encrypt(message, shift)    #import from crypto module
            print(f"Encrypted message: {encrypt_message}")
        else:
            decrypt_message = crypto.decrypt(message, shift)    #import from crypto module
            print(f"Decrypted message: {decrypt_message}")
    
    else:
        print("Please enter correct option from the MAIN MENU!")
