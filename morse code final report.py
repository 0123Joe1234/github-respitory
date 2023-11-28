morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z':'--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ' ': '/'
    }


def text_to_morse(text):
    

    text = text.upper()
    morse_code = ' '.join([morse_code_dict[char]for char in text if char in morse_code_dict])
    return morse_code


def morse_to_text(morse_code):
    morse_dict_reverse = {v: K for K, v in morse_code_dict.items()}
   
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        if code in morse_dict_reverse:
            text += morse_dict_reverse[code]
        else:
            text += 'UNKNOWN_CODE'
    return text

def get_encryption_input():
    return input("Enter a phrase to enrypt: ")

def get_decryption_input():
    return input("Enter Morse code to decrypt: ")

def main():
    while True:
        choice = input("Choose 'Encrypt' or 'Decrypt' (or 'Quit' to exit): ").capitalize()

        if choice == "Encrypt":
            phrase = get_encryption_input()
            encrypted_text = text_to_morse(phrase)
            print(f"Encrypted MOrse Code: {encrypted_text}")
        elif choice == "Decrypt":
            morse_input = get_decryption_input()
            decrypted_text = morse_to_text(morse_input)
            print(f"DEcrypted Text: {decrypted_text}")
        elif choice == "Quit":
            print("Exiting the program.")
            break
        else:
            print("Please enter 'Encrypt', 'Decrypt', or 'Quit'. ")

if __name__ == "__main__":
    main()                



 
