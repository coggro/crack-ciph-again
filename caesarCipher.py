# Caesar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

import pyperclip

# the string to be encrypted/decrypted
# message = input('Enter message: ')
message = 'What is dead may never die'

# The encryption/decryption key
# key = int(input('Enter en-/decryption key: '))
key = 13

# Tells the program to encrypt or decrypt
mode = 'encrypt' # set to 'encrypt' or 'decrypt'

# Every possible symbol that can be encrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''

# Capitalize the string in message
message = message.upper()

# Run the encryption/decryption code on each symbol in the message string
for symbol in message:
    if symbol in LETTERS:
        # Get the encrypted (or decrypted) number for this symbol
        num = LETTERS.find(symbol) # get the number of the symbol
        if mode == 'encrypt':
            num += key
        elif mode == 'decrypt':
            num -= key

        # Handle the wrap-around if num is larger than the length of
        # LETTERS or less than 0
        if num >= len(LETTERS):
            num -= len(LETTERS)
        elif num < 0:
            num += len(LETTERS)

        # Add encrypted/decrypted number's symbol at the end of translated
        translated += LETTERS[num]

    else:
        # Just add the symbol without encrypting/decrypting
        translated += symbol


# Print the encrypted/decrypted string to the screen
print(translated)

# Copy the encrypted/decrypted string to the clipboard
pyperclip.copy(translated)