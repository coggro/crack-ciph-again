# Caesar Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

message = 'GUVF VF ZL FRPERG ZRFNTR'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Loop through every possible key
for key in range(len(LETTERS)):

    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared.
    translated = ''

    # The rest of the program is the same as the original Caesar program
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num -= key

            # Handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num += len(LETTERS)
            elif num > len(LETTERS):
                num -= len(LETTERS)

            # Add number's sumbol at the end of translated
            translated += LETTERS[num]

        else:
            # Just add the symbol without en-/decrypting
            translated += symbol


    # Display the current key being tested, along with its description
    print('Key #%s: %s' % (key,translated))