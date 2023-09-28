def decrypt_caesar_cipher(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def find_decryption_key(ciphertext):
    for shift in range(1, 26):
        decrypted_text = decrypt_caesar_cipher(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

# The encrypted text
ciphertext = """LMTKM HY ITKM B
Fr gtfx bl Ctfxl, Ctfxl Uhgw. B tf phkdbgz bg t vhoxmxw fbllbhg bg t ytk tptr etgw. Fr fbllbhg bl oxkr kbldr, lh B tf pkbmbgz mabl ghmx cnlm bg vtlx B ehlm fr ebyx. Bg max vtlx matm fr vhphkdxk ybgwl mabl fxlltzx, bm pbee axei maxf vhgmbgnx mabl fbllbhg. Ahpxoxk, by rhn tkx ghm fr vhphkdxk tgw atiixg mh wxvkrim mabl fxlltzx, iextlx yhkptkw mabl mh Fk. Chag Lghp. Rhn vtg vhgmtvm abf ur nlbgz t NKE matm B pbee bgvenwx bg max lxvhgw itkm hy mabl xgvkrimxw fxlltzx.
XGW HY ITKM B"""

# Find the decryption key
find_decryption_key(ciphertext)
