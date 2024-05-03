alphebet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encryption(plain_text, shift_key):
    cipher_text = " "
    for char in plain_text:
        if char in alphebet:
            position = alphebet.index(char)
            new_position = (position+shift_key) % 26
            cipher_text += alphebet[new_position]
        else:
            cipher_text += char
    print(cipher_text)


def decryption(cipher_text, shift_key):
    plain_text = " "
    for char in cipher_text:
        if char in alphebet:
            position = alphebet.index(char)
            new_position = (position-shift_key) % 26
            plain_text += alphebet[new_position]
        else:
            plain_text += char
    print(plain_text)


end = False

while not end:
    Type = input("Type encrypt for Encryption OR decrypt for Decryption: ")
    Text = input("Enter your message: ")
    Shift = int(input("Enter shift key: "))

    if Type == "encrypt":
        encryption(plain_text=Text, shift_key=Shift)

    elif Type == "decrypt":
        decryption(cipher_text=Text, shift_key=Shift)

    play_again = input("Type 'yes' to continue and 'no' to exit  ")
    if play_again == 'no':
        end = True
