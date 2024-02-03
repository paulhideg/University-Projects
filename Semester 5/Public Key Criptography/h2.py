# Importing required libraries
import string

def bellaso_cipher_encrypt(message, key):
    """
    This function implements the Bellaso Cipher for encryption.
    
    Parameters:
    message (str): The message to be encrypted.
    key (str): The key used for encryption.
    
    Returns:
    str: The encrypted message.
    """
    
    # Defining the alphabet
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    
    # Making sure the key is at least as long as the message
    extended_key = key * (len(message) // len(key)) + key[:len(message) % len(key)]
    
    # Encrypting the message
    encrypted_message = ""
    for m, k in zip(message, extended_key):
        if m in alphabet:
            # Shifting the character by the key
            index = (alphabet.index(m) + alphabet.index(k)) % len(alphabet)
            encrypted_message += alphabet[index]
        else:
            encrypted_message += m
    
    return encrypted_message

def bellaso_cipher_decrypt(encrypted_message, key):
    """
    This function implements the Bellaso Cipher for decryption.
    
    Parameters:
    encrypted_message (str): The message to be decrypted.
    key (str): The key used for decryption.
    
    Returns:
    str: The decrypted message.
    """
    
    # Defining the alphabet
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    
    # Making sure the key is at least as long as the message
    extended_key = key * (len(encrypted_message) // len(key)) + key[:len(encrypted_message) % len(key)]
    
    # Decrypting the message
    decrypted_message = ""
    for em, k in zip(encrypted_message, extended_key):
        if em in alphabet:
            # Shifting the character by the key
            index = (alphabet.index(em) - alphabet.index(k)) % len(alphabet)
            decrypted_message += alphabet[index]
        else:
            decrypted_message += em
    
    return decrypted_message

# Testing the functions
message = "Hello World"
key = "KEY"  # A simple key for demonstration

encrypted_message = bellaso_cipher_encrypt(message, key)
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = bellaso_cipher_decrypt(encrypted_message, key)
print(f"Decrypted Message: {decrypted_message}")


#Lab3 PROBLEMA 2