
import sys

def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decode":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char

    return result


print("CAESAR CIPHER")
print("1. Encryption")
print("2. Decryption")

choice = input("Enter your choice: ")

text = input("Enter your message: ")
shift = int(input("Enter shift key: "))

if choice == "1":
    print("Encrypted message:", caesar_cipher(text, shift, "encode"))
elif choice == "2":
    print("Decrypted message:", caesar_cipher(text, shift, "decode"))
else:
    print("Invalid choice!")
