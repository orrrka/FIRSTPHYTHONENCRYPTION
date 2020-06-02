def sub_encrypt(plaintext, alphabet, shuffled):
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            position = alphabet.find(char)
            new_char = shuffled[position]
            #print(char, "-->", new_char)
            ciphertext = ciphertext + new_char
        else:
            ciphertext = ciphertext + char
            #print(char, "unchanged")

    return ciphertext

def caesar_encrypt5(plaintext):
    # Write your solution here (don't forget to use sub_encrypt!):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shuffled = alphabet
    plaintext= sub_encrypt(plaintext, alphabet, shuffled)
    encrypted= ""
    for char in plaintext:
        if char in alphabet:
            position2= shuffled.find(char) +5
            if position2 > 25:
               position2= position2 % 26
               char= shuffled[position2]
            else: char= shuffled[position2]
            
            encrypted= encrypted +char
        else:
            encrypted= encrypted +char
        
    return encrypted

# in order to find out a message-use: 
def sub_decrypt(ciphertext, alphabet, shuffled):
    plaintext = sub_encrypt(ciphertext, shuffled, alphabet)
    for char in ciphertext:
        if char in alphabet:
            position2= shuffled.find(char) -5
            if position2 > 25:
               position2= position2 % 26
               char= shuffled[position2]
            else: char= shuffled[position2]
            
            plaintext= plaintext +char
        else:
            plaintext= plaintext +char
        
    return plaintext

#write message after the inner braces :) 
print(caesar_encrypt5("i luv you have a nice day 3>"))