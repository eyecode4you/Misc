# learning_with_errors_encryption.py
import numpy as np
from matplotlib import pyplot as plt
""" N - no. of LWE samples - 1.1 . n log q
    q - modulus - a prime between n^2 and 2n^2
    n - security parameter (vector dimension)
    X - error distribution - Ψα, with α = 1/(√n log^2 n), 
    where Ψα is obtained by sampling the normal distribution
    N(0, α^2/(2π)) and reducing the result modulo 1 """

n = 8
q = 127
N = int(1.1 * n * np.log(q))
sigma = 1.0

print(f"n:{n}, q:{q}, N:{N}, sigma:{sigma}")

def chi(stdev, modulus):
    """ approximates random error/noise contributions
        drawn from a discrete Gaussian distribution
        with standard deviation """
    return round((np.random.randn() * stdev**2)) % modulus

sd = 2 # σ
m = 1000
for x in range(10):
    print("chi = ", chi(sd, m))

# generate private key - choose n values between 0 and q
alice_private_key = np.random.randint(0, high=q, size=n)
print(f"Alice's private key: {alice_private_key}")

# public key - generate the sample
alice_public_key = []

# N = number of values we want in key
for i in range(N):
    # n random values between 0 and <q
    a = np.random.randint(0, high=q, size=n)
    # get error to introduce
    epsilon = chi(sigma, q)
    # calc dot product
    b = (np.dot(a, alice_private_key) + epsilon) % q
    # value to be added to key
    sample = (a, b)
    alice_public_key.append(sample)
print(f"Alice's public key: {alice_public_key}")

""" Bob sends an encrypted message 
    To encrypt, bob selects arbitrary number of samples 
    at random from the public key to form the ciphertext 
    For this, he creates a mask, a random binary vector r of length N """
bob_message_bit = 1
print(f"\nBob's message bit: {bob_message_bit}")

r = np.random.randint(0, 2, N)
print(f"Bob's mask: {r}")

# Take mask and apply to relevant entry in public key, calculating sum of values found
sum_ai = np.zeros(n, dtype=int)
sum_bi = 0
for i in range(N):
    sum_ai = sum_ai + r[i] * alice_public_key[i][0]
    sum_bi = sum_bi + r[i] * alice_public_key[i][1]
sum_ai = [ x % q for x in sum_ai ]
ciphertext = (sum_ai, (bob_message_bit*int(np.floor(q/2))+sum_bi)%q)
print(f"Ciphertext: {ciphertext}")

""" Decryption """
adots = np.dot(ciphertext[0], alice_private_key) % q
b_adots = (ciphertext[1] - adots) % q

decrypted_message_bit = round((2*b_adots)/q) % 2

print(f"Original message bit: {bob_message_bit}, Decrypted message bit: {decrypted_message_bit}")
assert bob_message_bit == decrypted_message_bit

""" For encrypting longer bit strings, simply loop the operation """
bob_message_bits = np.random.randint(0, 2, 16) # 16 random binary bits
print(f"\nBob's message bits:\t {bob_message_bits}")
decrypted_bits = []

for ib in range(len(bob_message_bits)):
    bob_message_bit = bob_message_bits[ib]

    r = np.random.randint(0, 2, N)

    sum_ai = np.zeros(n, dtype=int)
    sum_bi = 0
    for i in range(N):
        sum_ai = sum_ai + r[i] * alice_public_key[i][0]
        sum_bi = sum_bi + r[i] * alice_public_key[i][1]
    sum_ai = [ x % q for x in sum_ai ]

    ciphertext = (sum_ai, (bob_message_bit*int(np.floor(q/2))+sum_bi)%q)
    adots = np.dot(ciphertext[0], alice_private_key) % q
    b_adots = (ciphertext[1] - adots) % q

    decrypted_message_bit = round((2*b_adots)/q) % 2
    assert decrypted_message_bit == bob_message_bit

    decrypted_bits.append(decrypted_message_bit)

assert np.all(decrypted_bits) == np.all(bob_message_bits)
print(f"Decrypted message bits:\t {np.array(decrypted_bits)}")
