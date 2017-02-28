
keyword = 'boomchacka'

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

text = 'move your troops to the designated location'


def viginere_square(key):
    shift_alph = []
    for letter in key:
        for index in range(len(alphabet)):
                    current_index = index
                    current_letter = alphabet[current_index]
                    if letter == current_letter:
                        shift_alph.append(alphabet[current_index:] + alphabet[:current_index])
    return shift_alph



def viginere_encrypt(message,key):

    encrypted_text = ''
    index = 0
    shift_alph = viginere_square(key)
    for letter in message:

        if letter == ' ':
            encrypted_text += ' '
        else:
                for index2 in range(len(alphabet)):
                    current_index = index2
                    current_letter = alphabet[current_index]

                    if letter == current_letter and index < len(shift_alph) -1:
                        row_alph = shift_alph[index]
                        new_letter = row_alph[current_index]
                        encrypted_text += new_letter
                        index += 1
                    elif letter == current_letter and index == len(shift_alph) -1:
                        row_alph = shift_alph[index]
                        new_letter = row_alph[current_index]
                        encrypted_text += new_letter
                        index = 0
    print encrypted_text
    return encrypted_text

def viginere_decrypt(encrypted_text,key):
    decrypted_text = ''
    index = 0
    shift_alph = viginere_square(key)
    for letter in encrypted_text:
        if letter == ' ':
            decrypted_text += ' '
        else:
            for symbol in shift_alph[index]:
                if letter == symbol:

                    if index < len(key) -1 :
                       new_index = shift_alph[index].index(symbol)
                       decrypted_letter = alphabet[new_index]
                       decrypted_text += decrypted_letter
                       index += 1

                    else:
                        index == len(key)
                        new_index = shift_alph[index].index(symbol)
                        decrypted_letter = alphabet[new_index]
                        decrypted_text += decrypted_letter
                        index = 0

    print decrypted_text


encrypted_text = viginere_encrypt(text, keyword)
viginere_decrypt(encrypted_text, keyword)
