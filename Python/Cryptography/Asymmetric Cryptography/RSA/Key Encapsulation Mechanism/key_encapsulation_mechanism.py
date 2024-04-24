# key_encapsulation_mechanism_rsa.py
""" In the following workflow, we illustrate the use of RSA to simulate a 
Key Encapsulation Mechanism (KEM) whereby a sufficiently long random 
secret message is securely exchanged and subsequently converted into 
a shared-secret of the appropriate length using a 
Key Derivation Function (KDF). """

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes, serialization
from os import urandom

# Gen Bob's RSA key-pair
private_key_bob = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key_bob = private_key_bob.public_key()
print("Bob's private key created!")

# Alice generates a long secret from which the shared secret will be derived
alice_long_secret = urandom(160) # 160-byte (1280-bit) random message
print("Alice's secret created!")

# Alice encrypts secret using Bob's public key, sent to Bob
""" we are using shorter secret than a pure KEM so we need padding 
(2048-bit RSA, random integer modulo the 2048-bit RSA modulus), 
cryptography library requires use of padding when encrypting 
with RSA. """
alice_encrypted_secret = public_key_bob.encrypt(
    alice_long_secret,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Alice's secret encrypted!")

# Bob decrypts secret using his private key
bob_decrypted_secret = private_key_bob.decrypt(
    alice_encrypted_secret,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

assert alice_long_secret == bob_decrypted_secret, "Secrets do not match!"

print("Secrets match!")

# Both Alice & Bob apply an agreed-upon KDF on secret to derive symmetric key
""" This involves hashing and a random salt - ensures uniqueness 
and unpredictability of shared symmetric key. The salt itself doesn't 
need to be secret, once it's generated, it can be broadcast alongside 
the encrypted secret. Assume Alic and Bob have access to 
the same random salt. """

def key_derivation_function(secret, salt):
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32, # Desired key length
        salt=salt,
        info=None,
        backend=None
    )
    return hkdf.derive(secret)

common_salt = urandom(16)

symmetric_key_alice = key_derivation_function(alice_long_secret, common_salt)
symmetric_key_bob = key_derivation_function(bob_decrypted_secret, common_salt)

assert symmetric_key_alice == symmetric_key_bob, "Derived keys do not match!"

print(f"A symmetric key of length {len(symmetric_key_alice)*8} bits was successfully derived by both Alice and Bob!")
