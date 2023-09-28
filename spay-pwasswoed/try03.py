import re

# Read the quadgrams and frequencies from the file
quadgrams = {}
with open('quadgrams.txt', 'r') as file:
    for line in file:
        quadgram, count = line.strip().split()
        count = int(count)
        quadgrams[quadgram] = count

# Given secret document
secret_document = """
This is a representational encoding using quadgrams.
"""

# Remove spaces and make all characters lowercase
secret_document = re.sub(r'[^a-zA-Z]', '', secret_document).lower()

# Function to calculate quadgram probabilities
def calculate_quadgram_probabilities(text):
    quadgram_probabilities = {}
    total_quadgrams = len(text) - 3  # Total number of quadgrams in the text

    for i in range(total_quadgrams):
        quadgram = text[i:i+4]
        if quadgram in quadgrams:
            probability = quadgrams[quadgram] / total_quadgrams
            quadgram_probabilities[quadgram] = probability

    return quadgram_probabilities

# Calculate quadgram probabilities for the secret document
document_quadgram_probabilities = calculate_quadgram_probabilities(secret_document)

# Replace quadgrams in the secret document with highest probability quadgrams from English
for quadgram, probability in document_quadgram_probabilities.items():
    highest_probability_quadgram = max(quadgrams, key=lambda x: quadgrams[x])
    secret_document = secret_document.replace(quadgram, highest_probability_quadgram)

print("Encrypted Text:")
print(secret_document)
