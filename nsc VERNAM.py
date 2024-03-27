class VernamCipher:
    def __init__(self, plaintext, key):
        self.plaintext = plaintext.upper()
        self.key = key.upper()
        self.validation()

    def validation(self):
        while True:
            if len(self.plaintext) == len(self.key):
                break
            else:
                print("Lengths of plaintext and key must be the same.", end="")
                self.key = input(" Enter the key: ").upper()

    def encrypt(self):
        encrypted_message = ''
        for char, k in zip(self.plaintext, self.key):
            encrypted_char = chr((ord(char) + ord(k) - 2 * ord('A')) % 26 + ord('A'))
            encrypted_message += encrypted_char
        return encrypted_message

    def decrypt(self):
        decrypted_message = ''
        for char, k in zip(self.plaintext, self.key):
            decrypted_char = chr((ord(char) - ord(k) + 26) % 26 + ord('A'))
            decrypted_message += decrypted_char
        return decrypted_message

    def display_results(self):
        print("Original Message:", self.plaintext)
        print("Encrypted Message:", self.encrypt())
        print("Decrypted Message:", self.decrypt())

plaintext_input = input("Enter plaintext: ")
key_input = input("Enter key: ")
encryption = VernamCipher(plaintext_input, key_input)
encryption.display_results()

