def vigenere_encrypt(text, key):
    key = (key * (len(text) // len(key) + 1))[:len(text)].lower()
    encrypted = ""
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i]) - 97
            encrypted += chr((ord(char.lower()) - 97 + shift) % 26 + 97).upper() if char.isupper() else chr((ord(char.lower()) - 97 + shift) % 26 + 97)
        else:
            encrypted += char
    return encrypted

def vigenere_decrypt(cipher, key):
    key = (key * (len(cipher) // len(key) + 1))[:len(cipher)].lower()
    decrypted = ""
    for i, char in enumerate(cipher):
        if char.isalpha():
            shift = ord(key[i]) - 97
            decrypted += chr((ord(char.lower()) - 97 - shift) % 26 + 97).upper() if char.isupper() else chr((ord(char.lower()) - 97 - shift) % 26 + 97)
        else:
            decrypted += char
    return decrypted

# Example
text = "lifeisfullofsurorises"
key = "health"
cipher = vigenere_encrypt(text, key)
plain = vigenere_decrypt(cipher, key)
print("Vigenere Encrypted:", cipher)
print("Vigenere Decrypted:", plain)
