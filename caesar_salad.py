def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

while True:
    try:
        input_choice = input('Enter if encryption or decryption: ')
        if (input_choice == 'encryption' or input_choice.lower() == 'encryption'):
            encrypt = True
        elif (input_choice == 'decryption' or input_choice.lower() == 'decryption'):
            encrypt = False
        else:
            raise ValueError
    except ValueError:
        pass
    print('Invalid input. Please try again.')
        

    try:
        input_text = input("Enter the text to be encrypted or decrypted: ")
    except isinstance(input_text, str) == False:
        print('Text must be a string. Please try again. \n')

    try:
        input_shift = input("Enter the shift of the text: ")
    except isinstance(input_text, int) == False:
        print('Text must be an integer. Please try again. \n')