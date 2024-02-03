import random

# Rabin algorithm is based on squaring each ASCII value modulo the product of two randomly generated prime numbers (p and q). 

# Function to check if a number is prime
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    return True

# Function to generate public and private keys
def generateKeys():
    p = 0
    q = 0
    interval_lower_bound = random.randint(0, 150)
    interval_upper_bound = random.randint(151, 300)
    
    # Ensure p and q are prime, not equal, and satisfy a specific condition
    #In the Rabin cryptosystem, the security relies on the difficulty of factoring the modulus n = p * q, where p and q are large prime numbers. 
    while isPrime(p) is False or isPrime(q) is False or p == q or (p % 4 != q % 4 or p % 4 != 3):
        p = random.randint(interval_lower_bound, interval_upper_bound)
        q = random.randint(interval_lower_bound, interval_upper_bound)
        
    return p, q

# Function to check if plaintext contains valid characters
def plaintextIsValid(plaintext, alphabet):
    for character in plaintext:
        if character not in alphabet:
            return False
    return True

# Function to check if ciphertext contains valid data types
def ciphertextIsValid(ciphertext):
    for n in ciphertext:
        if isinstance(n, (int, float, complex)):
            return False
    return True

# Function to convert plaintext to ASCII value
def convertPlaintextToASCII(plaintext):
    m = int.from_bytes(plaintext.encode('ascii'), byteorder='big')
    return m

# Function to convert ASCII value to plaintext
def convertASCIIToPlaintext(ascii_value):
    if 0 <= ascii_value <= 128:
        byte_data = ascii_value.to_bytes((ascii_value.bit_length() + 7) // 8, 'big')
        plaintext = byte_data.decode('ascii')
        return plaintext
    return "?"

# Function to convert a number to binary string
def convertToBinary(m):
    if m > 0:
        return str(bin(int(m % 256))[2:])
    else:
        return str(bin(int((256 + m) % 256))[3:])

# Function to extend a binary string
def extendBinary(m):
    x = str(m) + str(m)
    return int(x)

# Function to transform binary to decimal
def transformToDecimal(m):
    return int(m, 2)

# Function to encrypt a number
def encrypt(m, n):
    return (m * m) % n

# Extended Euclidean Algorithm for finding modular inverse
def extended_gcd(p, q):
    if p == 0:
        return q, 0, 1
    else:
        gcd, x, y = extended_gcd(q % p, p)
        return gcd, y - (q // p) * x, x

# Function to divide binary string into two halves
def divide_in_half(binary_string):
    length = len(binary_string)
    half_length = length // 2
    first_half = binary_string[:half_length]
    second_half = binary_string[half_length:]
    return first_half, second_half

# Function to convert plaintext to list of ASCII values
def convertPlaintextToASCIIList(plaintext):
    ascii_list = []
    for character in plaintext:
        ascii_list.append(convertPlaintextToASCII(character))
    return ascii_list

# Function to encrypt a list of numbers
def encryptList(m, n):
    encrypted_list = []
    for number in m:
        encrypted_list.append(encrypt(number, n))
    return encrypted_list

# Function to find the correct choice among four possibilities
def findRightChoice(m1, m2, m3, m4):
    if m1 != "?":
        return m1
    if m2 != "?":
        return m2
    if m3 != "?":
        return m3
    if m4 != "?":
        return m4

# Function to decrypt a character
def decryptCharacter(character, a, b, p, q, n):
    print(f"The character is {character}.")

    # Using the Rabin decryption formula
    mp = pow(character, (p + 1) // 4, p)
    mq = pow(character, (q + 1) // 4, q)

    X = (a * p * mq + b * q * mp) % n
    Y = (a * p * mq - b * q * mp) % n

    m1 = X
    m2 = n - X
    m3 = Y
    m4 = n - Y

    m1 = convertASCIIToPlaintext(m1)
    m2 = convertASCIIToPlaintext(m2)
    m3 = convertASCIIToPlaintext(m3)
    m4 = convertASCIIToPlaintext(m4)

    return findRightChoice(m1, m2, m3, m4)

if __name__ == '__main__':
    # Generate public and private keys
    p, q = generateKeys()
    n = p * q
    print(f"p = {p}\nq = {q}\nn = p * q = {n}")

    print(f"The public key is {n}, the private key is ({p}, {q}).\n")

    print("ENCRYPTION:")
    plaintext = input("What is the message you would like to encrypt?\nMessage:")
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z',
                ' ']

    # Check if plaintext is valid
    if plaintextIsValid(plaintext, alphabet) is False:
        print("Plaintext is not valid!!!")
    else:
        print("Plaintext is valid.")

        m = convertPlaintextToASCIIList(plaintext)
        print(f"The converted message to ASCII value is {m}.")

        # Encrypt ASCII list
        # Each ASCII value in the list is squared modulo the product of the two randomly generated prime numbers (p and q).
        m = encryptList(m, n)
        print(f"The encrypted message is {m}.\n\n\n")

        print("DECRYPTION:")
        ciphertext = m
        print(f"The ciphertext C is {ciphertext}.")

        # Check if ciphertext is valid
        if ciphertextIsValid(plaintext) is False:
            print("Ciphertext is not valid!!!")
        else:
            print("Ciphertext is valid.")

        # Find modular inverse using Extended Euclidean Algorithm
        # calculates the greatest common divisor (gcd) and the coefficients a and b such that a * p + b * q = gcd(p, q).
        # These coefficients are crucial for finding the modular inverse.
        gcd, a, b = extended_gcd(p, q)
        if gcd == 1:
            print(f"a:{a}, b: {b}, a * p + b * q = {a * p + b * q}")
        else:
            print(f"No solution exists as gcd({p}, {q}) != 1")

        decrypted_message = ""
        for character in ciphertext:
            decrypted_message += decryptCharacter(character, a, b, p, q, n)

        print(f"The decrypted message is {decrypted_message}.")

        # Convert plaintext to ASCII list
        
