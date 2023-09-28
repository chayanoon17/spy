import random

# Given substitution key
substitution_key = "bcadefghijklmnopqrstuvwxyz"

# Create a dictionary to represent the mapping from normal letters to substituted letters
substitution_dict = {chr(97 + i): substitution_key[i] for i in range(26)}

# Inverse dictionary for decryption
inverse_substitution_dict = {v: k for k, v in substitution_dict.items()}

# Given frequency of letters in English
english_letter_frequency = {
    'a': 79, 'b': 14, 'c': 27, 'd': 41, 'e': 122, 'f': 21, 'g': 19, 'h': 59, 'i': 68, 'j': 2,
    'k': 8, 'l': 39, 'm': 23, 'n': 65, 'o': 72, 'p': 18, 'q': 1, 'r': 58, 's': 61, 't': 88,
    'u': 27, 'v': 10, 'w': 23, 'x': 2, 'y': 19, 'z': 10
}

# Function to encrypt a plaintext
def encrypt(plaintext):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                substituted_char = substitution_dict[char]
            else:
                substituted_char = substitution_dict[char.lower()].upper()
            ciphertext += substituted_char
        else:
            ciphertext += char
    return ciphertext

# Generate a sample plaintext
sample_plaintext = "It is a representational encoding."

# Encrypt the plaintext
encrypted_text = encrypt(sample_plaintext)
print("Encrypted Text:", encrypted_text)

# Function to calculate letter frequency in the text
def calculate_letter_frequency(text):
    frequency = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency

# Calculate letter frequency in the encrypted text
encrypted_letter_frequency = calculate_letter_frequency(encrypted_text)

# Compare with English letter frequency
for letter, english_frequency in english_letter_frequency.items():
    encrypted_frequency = encrypted_letter_frequency.get(letter, 0)
    print(f"Letter '{letter}': English Frequency={english_frequency}, Encrypted Frequency={encrypted_frequency}")

# Decryption function
def decrypt(ciphertext):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                original_char = inverse_substitution_dict[char]
            else:
                original_char = inverse_substitution_dict[char.lower()].upper()
            plaintext += original_char
        else:
            plaintext += char
    return plaintext

# Decrypt the encrypted text
decrypted_text = decrypt(encrypted_text)
print("Decrypted Text:", decrypted_text)
