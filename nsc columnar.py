import math

def encrypt_columnar_cipher(plaintext, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_columns = len(key)
    num_rows = math.ceil(len(plaintext) / num_columns)
    grid = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]
    
    for i, char in enumerate(plaintext):
        row = i // num_columns
        col = key_order[i % num_columns]
        grid[row][col] = char
    
    cipher_text = ''.join([''.join(row) for row in grid])
    return cipher_text

def decrypt_columnar_cipher(cipher_text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_columns = len(key)
    num_rows = math.ceil(len(cipher_text) / num_columns)
    grid = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]
    
    char_index = 0
    for col in key_order:
        for row in range(num_rows):
            if char_index < len(cipher_text):
                grid[row][col] = cipher_text[char_index]
                char_index += 1
    
    plaintext = ''.join([''.join(row) for row in grid])
    return plaintext

def main():
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key (a permutation of numbers indicating column order): ").split()
    key = [int(k) for k in key]

    encrypted_text = encrypt_columnar_cipher(plaintext, key)
    print("Encrypted text:", encrypted_text)

    decrypted_text = decrypt_columnar_cipher(encrypted_text, key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
