# diffie-hellman.py
# 1: Alice and Bob agree on a prime number p and primitive root a e.g. 11 and 7
p = 11
a = 7
print(f"Prime: {p}")
print(f"Primitive Root: {a}")

# 2: Alice choses a secret exponent Ka and calculates Ha = a^ka (mod p)
K_a = 4 # Alice's private key
H_a = (a**(K_a)) % p # Alice's public key
print(f"\nAlice private: {K_a} and public: {H_a}")

# 3: Bob does the same with his own secret
K_b = 8 # Bob's private key
H_b = (a**(K_b)) % p # Bob's public key

print(f"Bob private: {K_b} and public: {H_b}")

# 4: The two parties exchange their public keys Ha and Hb

# 5: Each party combines their private key with the other's public key to create a shared secret key
secret_key_alice = H_b**K_a % p
secret_key_bob = H_a**K_b % p
assert secret_key_alice == secret_key_bob
print(f"\nShared secret key: {secret_key_bob}")
