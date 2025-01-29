import random

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def mod_inverse(a, p):
    t, new_t = 0, 1
    r, new_r = p, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    return t + p if t < 0 else t

def encrypt_message(p, g, y, m):
    r = random.randint(1, p - 2)
    c1 = mod_exp(g, r, p)
    c2 = (m * mod_exp(y, r, p)) % p
    return c1, c2

def decrypt_message(p, c1, c2, x):
    inverse_c1 = mod_exp(c1, p - 1 - x, p)
    return (c2 * inverse_c1) % p

def encrypt_string(message, p, g, y):
    encrypted_c1, encrypted_c2 = [], []
    for char in message:
        c1, c2 = encrypt_message(p, g, y, ord(char))
        encrypted_c1.append(c1)
        encrypted_c2.append(c2)
    return encrypted_c1, encrypted_c2

def decrypt_string(encrypted_c1, encrypted_c2, p, x):
    decrypted_message = "".join(
        chr(decrypt_message(p, c1, c2, x)) for c1, c2 in zip(encrypted_c1, encrypted_c2)
    )
    return decrypted_message

def main():
    p = int(input("Enter a large prime number p: "))
    g = int(input("Enter a primitive root g modulo p: "))
    x = int(input("Enter private key x: "))
    y = mod_exp(g, x, p)
    print(f"Public Key: (p = {p}, g = {g}, y = {y})")
    message = input("Enter the message to encrypt (string or number): ")
    if message.isdigit():
        m = int(message)
        c1, c2 = encrypt_message(p, g, y, m)
        decrypted_message = decrypt_message(p, c1, c2, x)
        print(f"\nEncrypted Message: (c1 = {c1}, c2 = {c2})")
        print(f"Decrypted Message: {decrypted_message}")
    else:
        encrypted_c1, encrypted_c2 = encrypt_string(message, p, g, y)
        decrypted_message = decrypt_string(encrypted_c1, encrypted_c2, p, x)
        print("\nEncrypted Message:", list(zip(encrypted_c1, encrypted_c2)))
        print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
