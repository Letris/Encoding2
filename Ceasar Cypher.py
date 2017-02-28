alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

text = 'move your troops to the designated location'

encryption_letter_move = 13
decryption_letter_move = 13



def encrypt(message):
    encrypted_text = ''
    for letter in message:
        if letter == ' ':
            encrypted_text += ' '
        else:
            for index in range(len(alphabet)):
                current_index = index
                current_letter = alphabet[index]
                if letter == current_letter and current_letter != 'z':
                        new_index = current_index + encryption_letter_move
                        if new_index >= len(alphabet) - 1:
                            difference = new_index - len(alphabet)
                            newer_index = 0 + difference
                            new_letter = alphabet[newer_index]
                            encrypted_text += new_letter
                        else:
                            new_letter = alphabet[new_index]
                            encrypted_text += new_letter
                elif letter == current_letter and letter == 'z':
                     new_index = encryption_letter_move -1
                     newer_letter = alphabet[new_index]
                     final_letter = newer_letter
                     encrypted_text += final_letter



    print encrypted_text
    return encrypted_text

def decrypt(message):
    decrypted_text = ''
    for letter in message:
        if letter == ' ':
            decrypted_text += ' '
        else:
            for index in range(len(alphabet)):
                current_index = index
                current_letter = alphabet[index]
                if letter == current_letter and letter != 'a':
                    new_index = current_index - decryption_letter_move
                    new_letter = alphabet[new_index]
                    decrypted_text += new_letter
                elif letter == current_letter and letter == 'a':
                    new_index = len(alphabet) - decryption_letter_move
                    decrypted_text += alphabet[new_index]

    print decrypted_text


encrypted_text = encrypt(text)
decrypt(encrypted_text)