# symmetric_crypto.py - Example of Caesar Cipher & AES
from secretpy import Caesar
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from functools import reduce
import numpy as np

# Message (plaintext) to encrypt, only using lowercase
plaintext = u"this is a strict top secret message for intended recipients only"
print(f"\nGiven Plaintext: {plaintext}")

""" CAESAR CIPHER """
# Init. for Caesar shift
caesar_cipher = Caesar()

# Define shift (key)
caesar_key = 5
print(f"Caesar shift secret key: {caesar_key}")

# Define alphabet
alphabet=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ')
print(f"Alphabet: {alphabet}")

# Encrypt message
caesar_ciphertext = caesar_cipher.encrypt(plaintext, caesar_key, alphabet)
print(f"Encrypted Caesar Shift Ciphertext: {caesar_ciphertext}")

# Decrypt back to plaintext
caesar_plaintext = caesar_cipher.decrypt(caesar_ciphertext, caesar_key, alphabet)
print(f"Decrypted message: {caesar_plaintext}\n")

""" AES - key length 16 means message length must be a multiple of 16 as we're using CBC mode """
# lamba defines an inline function in this case that takes two values a,b with the resulting expression of a+b
# reduce uses a two-argument function(above), and applies this to all the entries in the list (random alphabet characters) cumulatively
aes_key = reduce(lambda a, b: a + b, [np.random.choice(alphabet) for i in range(16)])
print(f"AES secret key: {aes_key}")

# Init vector (nonce) will be used in Cipher Block Chaining (CBC) - additional randomness
aes_init_vector = reduce(lambda a, b: a + b, [np.random.choice(alphabet) for i in range(16)])
print(f"AES init vector: {aes_init_vector}")

# Encryptor setup using key & CBC. For both we convert string to bytes
sender_aes_cipher = Cipher(algorithms.AES(bytes(aes_key, 'utf-8')), modes.CBC(bytes(aes_init_vector, 'utf-8')))
aes_encryptor = sender_aes_cipher.encryptor()

# Update adds text to encrypt in chunks, finalize completes encryption
aes_ciphertext = aes_encryptor.update(bytes(plaintext, 'utf-8')) + aes_encryptor.finalize()

# Output is string of bytes
print(f"\nEncrypted AES ciphertext: {aes_ciphertext}")

# Decryption
receiver_aes_cipher = Cipher(algorithms.AES(bytes(aes_key, 'utf-8')), modes.CBC(bytes(aes_init_vector, 'utf-8')))
aes_decryptor = receiver_aes_cipher.decryptor()

aes_plaintext_bytes = aes_decryptor.update(aes_ciphertext) + aes_decryptor.finalize()
aes_plaintext = aes_plaintext_bytes.decode('utf-8')

print(f"\nDecrypted AES plaintext: {aes_plaintext}")
