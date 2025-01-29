def extended_euclidean(a, b):
    """
    Implements the Extended Euclidean Algorithm.
    Returns gcd(a, b) and the coefficients x, y such that:
    a * x + b * y = gcd(a, b)
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_euclidean(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

def multiplicative_inverse(a, m):
    """
    Finds the multiplicative inverse of a number a modulo m using Extended Euclidean Algorithm.
    Returns the inverse if it exists, otherwise returns None.
    """
    gcd, x, _ = extended_euclidean(a, m)
    if gcd != 1:
        return None  # Inverse doesn't exist
    else:
        return x % m  # Return positive inverse modulo m

# Example usage
if __name__ == "__main__":
    a = int(input("Enter the number to find the multiplicative inverse (a): "))
    m = 26  # We are working in Z26 (modulo 26)

    inverse = multiplicative_inverse(a, m)

    if inverse is None:
        print(f"The number {a} does not have a multiplicative inverse in Z26.")
    else:
        print(f"The multiplicative inverse of {a} modulo 26 is: {inverse}")
