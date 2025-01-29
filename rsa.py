import math

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def encrypt(m, e, n):
    return pow(m, e, n)  # Using Python's built-in modular exponentiation

def decrypt(c, d, n):
    return pow(c, d, n)

def encrypt_string(message, e, n):
    return [encrypt(ord(char), e, n) for char in message] + [-1]  # End marker

def decrypt_string(encrypted_message, d, n):
    return ''.join(chr(decrypt(c, d, n)) for c in encrypted_message if c != -1)

def main():
    p = int(input("Enter a prime number p: "))
    q = int(input("Enter a prime number q: "))
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = int(input("Enter the public exponent e: "))
    d = mod_inverse(e, phi)
    
    message = input("Enter the message to encrypt (string or number): ")
    
    if message.isdigit():  # If input is a number
        m = int(message)
        c = encrypt(m, e, n)
        decrypted_message_num = decrypt(c, d, n)
        print("\nEncrypted Message:", c)
        print("Decrypted Message:", decrypted_message_num)
    else:
        encrypted_message = encrypt_string(message, e, n)
        decrypted_message = decrypt_string(encrypted_message, d, n)
        print("\nEncrypted Message:", ' '.join(map(str, encrypted_message[:-1])))
        print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
