def caesar(text, shift, encrypter=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypter:
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
        input_choice = input('Enter if encryption or decryption: ').lower()
        if input_choice == 'encryption':
            encrypter = True
        elif input_choice == 'decryption':
            encrypter = False
        else:
            raise ValueError
        pass
        input_text = input("Enter the text to be encrypted or decrypted: ")
        input_shift = int(input("Enter the shift of the text (1-25): "))
        if input_shift < 1 or input_shift > 25:
            print('Shift must be an integer between 1 and 25.')
            raise ValueError
        
        if (input_choice == 'encryption' or input_choice.lower() == 'encryption'):
            print(encrypt(input_text, input_shift))
        elif (input_choice == 'decryption' or input_choice.lower() == 'decryption'):
            print(decrypt(input_text, input_shift))
        
        input_cont = input("Try again? (Y/N): ").upper()
        if input_cont == 'Y':
            pass
        elif input_cont == 'N':
            break
        else:
            raise ValueError
        
    except ValueError:
        pass
        print('Invalid input. Please try again.')