alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type the message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Combining the encrypt and decrypt functions into a single function called 'caesar_cipher'

def caesar_cipher(plain_text, cipher_text, shift_amount):
   
    if direction == "encode":
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

    
    if direction == "decode":
        plain_text = ""
        for letter in cipher_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            plain_text += new_letter
        print(f"The decoded text is {plain_text}")

# calling the fuction:
caesar_cipher(plain_text=text, cipher_text=text, shift_amount=shift)

