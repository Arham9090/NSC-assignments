def to_lowercase(text):
    return text.lower()

def remove_spaces(text):
    new_text = ""
    for char in text:
        if char != " ":
            new_text += char
    return new_text

def group_by_two(text):
    groups = []
    group = 0
    for i in range(2, len(text), 2):
        groups.append(text[group:i])
        group = i
    groups.append(text[group:])
    return groups

def fill_letter(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i + 1]:
                new_word = text[0:i + 1] + 'x' + text[i + 1:]
                new_word = fill_letter(new_word)
                break
            else:
                new_word = text
    else:
        for i in range(0, k - 1, 2):
            if text[i] == text[i + 1]:
                new_word = text[0:i + 1] + 'x' + text[i + 1:]
                new_word = fill_letter(new_word)
                break
            else:
                new_word = text
    return new_word

def generate_key_table(key, alphabet):
    key_letters = []
    for char in key:
        if char not in key_letters:
            key_letters.append(char)
    complement_elements = []
    for char in key_letters:
        if char not in complement_elements:
            complement_elements.append(char)
    for char in alphabet:
        if char not in complement_elements:
            complement_elements.append(char)
    matrix = []
    while complement_elements:
        matrix.append(complement_elements[:5])
        complement_elements = complement_elements[5:]
    return matrix

def search(matrix, element):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == element:
                return i, j

def encrypt_row_rule(matrix, row1, col1, row2, col2):
    char1 = matrix[row1][(col1 + 1) % 5]
    char2 = matrix[row2][(col2 + 1) % 5]
    return char1, char2

def encrypt_column_rule(matrix, row1, col1, row2, col2):
    char1 = matrix[(row1 + 1) % 5][col1]
    char2 = matrix[(row2 + 1) % 5][col2]
    return char1, char2

def encrypt_rectangle_rule(matrix, row1, col1, row2, col2):
    char1 = matrix[row1][col2]
    char2 = matrix[row2][col1]
    return char1, char2

def encrypt_by_playfair_cipher(matrix, plain_list):
    cipher_text = []
    for pair in plain_list:
        char1 = 0
        char2 = 0
        row1, col1 = search(matrix, pair[0])
        row2, col2 = search(matrix, pair[1])
        if row1 == row2:
            char1, char2 = encrypt_row_rule(matrix, row1, col1, row2, col2)
        elif col1 == col2:
            char1, char2 = encrypt_column_rule(matrix, row1, col1, row2, col2)
        else:
            char1, char2 = encrypt_rectangle_rule(matrix, row1, col1, row2, col2)
        cipher_text.append(char1 + char2)
    return cipher_text

text_plain = "Hello World"
text_plain = remove_spaces(to_lowercase(text_plain))
plain_text_list = group_by_two(fill_letter(text_plain))

if len(plain_text_list[-1]) != 2:
    plain_text_list[-1] = plain_text_list[-1] + 'z'

key = "example"
key = to_lowercase(key)
print("Key text:", key)
print("Plain Text:", text_plain)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
matrix = generate_key_table(key, alphabet)
cipher_list = encrypt_by_playfair_cipher(matrix, plain_text_list)
cipher_text = ""
for pair in cipher_list:
    cipher_text += pair

print("CipherText:", cipher_text)
