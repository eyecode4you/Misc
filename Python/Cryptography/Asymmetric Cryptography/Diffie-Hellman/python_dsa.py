# python_dsa.py
# Demonstrating the Digital Signature Algorithm (DSA)

""" 1: Key generation:
    we need public integers p, q, and g.
        p & q are two primes: 
            p with length N - usually 256-bits
            q with length L - usually 3072 bits
    
        g is used to gen cyclic subgroup of prime order q<p
        - refer to the Discrete Logarithm Problem (DLP)
    we need a hash function to convert from strings of length L to N

    From this we choose a random number x as private key and can 
    calculate a public key

    2: Key distribution:
        The following are shared:
            - p, q, g which describe the algorith
            - Hash function H
            - Public key y

    3: Signing:
        - message m can now be signed
        - resulting signature is (r, s)
        - message sent

    4: Verification:
        - receiver can verify sender is someone who has access to 
        private key x using all the public info: 
        q, p, g, H, y, (r, s), m    """

from random import randint
""" Assert:
- p, q are both prime 
- (p-1) mod q = 0
- g >= (p-2) 
- g^(p-1)/q mod p != 1 """

q=11
p=23
g=4

assert( (p-1) % q == 0 ), "!: (p-1) % q must == 0, try using different value for p or q"
assert( g>=2), "!: g must be >= 2"
assert( g <= (p-2) ), "!: g must <= (p-2), try using different value for g or p"
assert( (pow(g, (p-1)/q) % p) != 1 ), "!: try using different value for p, q, or g"

print(f"Public info is good: q={q}, p={p}, g={g}")

""" Next, the signer generates their private key
private key k must satisfy:
- k >= 2
- k <= (q-1) """

# choose rand int from {2..q-1}
private_key = randint(2, q-1)

assert(private_key >= 2)
assert(private_key <= (q-1))

print(f"\nPrivate Key: {private_key}")

""" Compute public key with modular exponentiation. 
    - reversing this to recover private key is an instance of DLP, 
    difficult to compute when large primes are used 
    
    public key y = g^x mod p """
public_key = pow(g, private_key, p)
# (g ** private_key) % p
print(f"Public Key: {public_key}")

""" Digital Signature - gen a hash H of the message m to sign 
assume a shared hash algorithm with hash length N equal to bits in q
"""

hash_dict={}
def mock_hash_func(inp):
    print("\nMessage:",inp)
    if not inp in hash_dict:
        hash_dict[inp] = randint(1, q)
    return hash_dict[inp]

message = "Encryption is really fun!"
message_hash = mock_hash_func(message) # in reality we'd use a hash function
print(f"\nMessage Hash is: {message_hash}")

""" Next, the sender generates a random per-message secret k as 
    well as its multiplicative inverse modulo q to 
    compute the signature (r, s):
        - r = (g^k mod p) mod q
        - s = (k^-1(H(m) + xr)) mod q
    !: we need to chose different value for k in the case where 
    either r or s compute to 0. """
signed=False
while(signed==False):
    k = randint(1, q-1)
    print("Using random k:", k)

    r = pow(g, k, p) % q # get modular inverse

    if(r == 0):
        print(f"{k} isn't a good random value to calculate r. Trying another...")
        continue

    s = (pow(k, -1, q) * (message_hash + private_key * r)) % q
    if(s==0):
        print(f"{k} isn't a good random value to calculate s. Trying another...")
        continue
    signed=True

signature = (r, s)
print(f"\nSignature: {signature}")

""" Message is broadcasted to receiver/verifier - has the 
    sender's public key
    
    Receiver will perform checks and re-generate hash of message
    and compute auxiliary quantities w, u1, u2, and v:
    - 0 < r < q
    - 0 < s < q
    - w = s^-1 mod q
    - u1 = H(m).w mod q
    - u2 = r.w mod q
    - v = ((g^u1)(y^u2) mod p) mod q 
    - Finally, receiver checks if v = r. If true, signature is
    verified """

# Receiver re-generates message hash
my_hash = mock_hash_func(message)
print(f"\nSent message hash: {my_hash}")

# Receiver computes auxiliary quantities w (using mod inverse), u1, u2, and v
w = (pow(s, -1, q)) % q
u1 = (my_hash * w) % q
u2 = (r * w) % q
v = ((g**u1 * public_key**u2) % p) % q

if v == r:
    print("Signature is Valid!")
else:
    print("Signature is Invalid!")