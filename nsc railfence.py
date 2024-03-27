def encrypt_rail_fence(text, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for char in text:
        fence[rail].append(char)
        rail += direction
        
        if rail == rails - 1 or rail == 0:
            direction *= -1
        
    cipher_text = ''.join([''.join(rail) for rail in fence])
    return cipher_text

def decrypt_rail_fence(cipher_text, rails):
    fence = [['' for _ in range(len(cipher_text))] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for i in range(len(cipher_text)):
        fence[rail][i] = '*'
        rail += direction
        
        if rail == rails - 1 or rail == 0:
            direction *= -1
    
    index = 0
    for i in range(rails):
        for j in range(len(cipher_text)):
            if fence[i][j] == '*' and index < len(cipher_text):
                fence[i][j] = cipher_text[index]
                index += 1
                
    rail = 0
    direction = 1
    plain_text = ''
    for i in range(len(cipher_text)):
        plain_text += fence[rail][i]
        rail += direction
        
        if rail == rails - 1 or rail == 0:
            direction *= -1
    
    return plain_text

def main():
    text = input("Enter the text to encrypt: ")
    rails = int(input("Enter the number of rails: "))
    
    encrypted_text = encrypt_rail_fence(text, rails)
    print("Encrypted text:", encrypted_text)
    
    decrypted_text = decrypt_rail_fence(encrypted_text, rails)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
