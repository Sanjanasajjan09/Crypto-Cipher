def affine_encrypt(text, a, b):
    encrypted = ""
    for char in text:
        if char.isalpha():
            x = ord(char.lower()) - 97
            encrypted += chr(((a * x + b) % 26) + 97).upper() if char.isupper() else chr(((a * x + b) % 26) + 97)
        else:
            encrypted += char
    return encrypted

def affine_decrypt(cipher, a, b):
    m = 26
    a_inv = pow(a, -1, m)  # Modular inverse
    decrypted = ""
    for char in cipher:
        if char.isalpha():
            y = ord(char.lower()) - 97
            decrypted += chr((a_inv * (y - b) % m) + 97).upper() if char.isupper() else chr((a_inv * (y - b) % m) + 97)
        else:
            decrypted += char
    return decrypted

# Example
text = "hello"
a, b = 7, 2
cipher = affine_encrypt(text, a, b)
plain = affine_decrypt(cipher, a, b)
print("Affine Encrypted:", cipher)
print("Affine Decrypted:", plain)