# auth_key_exchange_diffie-hellman_and_dsa
# A & B first agree on set of DH parameters and gen key pairs
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh, dsa
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization

# gen dh parameters
parameters = dh.generate_parameters(generator=2, key_size=2048)

# gen A's DH key pair
a_dh_private_key = parameters.generate_private_key()
a_dh_public_key = a_dh_private_key.public_key()

# gen B's DH key pair
b_dh_private_key = parameters.generate_private_key()
b_dh_public_key = b_dh_private_key.public_key()

print("Public & private keys generated for A & B!")

""" DH public keys are broadcast. Next, both Alice and Bob each 
    generate a separate key pair for use with DSA. These keys will 
    in turn be used to sign the DH public keys to be exchanged. """
# Generate DSA keys for Alice and Bob
a_dsa_private_key = dsa.generate_private_key(key_size=2048)
a_dsa_public_key = a_dsa_private_key.public_key()
b_dsa_private_key = dsa.generate_private_key(key_size=2048)
b_dsa_public_key = b_dsa_private_key.public_key()

print("Additional key pair generated for signing")

# Alice signs her DH public key using her DSA private key
a_public_bytes = a_dh_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo)
a_signature = a_dsa_private_key.sign(a_public_bytes, hashes.SHA256())

print("Alice signed public key")

# And Bob
b_public_bytes = b_dh_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo)
b_signature = b_dsa_private_key.sign(b_public_bytes, hashes.SHA256())

print("Bob signed public key")

""" DH public keys and signatures are now broadcasted. Each verifies the 
    other's public key and signature """
# Alice and Bob verify each other's DH public keys using DSA public keys
# An InvalidSignature exception will occur if they are not valid
a_dsa_public_key.verify(a_signature, a_public_bytes, hashes.SHA256())
b_dsa_public_key.verify(b_signature, b_public_bytes, hashes.SHA256())

print("Signatures are valid")

""" Following signature verification, Alice and Bob generate the 
    shared secret, which completes the key exchange """
# Perform key exchange
a_shared_key = a_dh_private_key.exchange(b_dh_public_key)
b_shared_key = b_dh_private_key.exchange(a_dh_public_key)

print("Shared secrets generated")

""" Optionally, for additional security, Alice and Bob can use a 
    specialized key derivation function such as HKDF to generate a 
    more secure symmetric key from their shared secret using key 
    stretching techniques """
# Derive a shared symmetric key using key-stretching
def derive_key(shared_key):
    return HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=None,
    ).derive(shared_key)

a_symmetric_key = derive_key(a_shared_key)
b_symmetric_key = derive_key(b_shared_key)

assert a_symmetric_key == b_symmetric_key
print("Keys checked to be the same")
