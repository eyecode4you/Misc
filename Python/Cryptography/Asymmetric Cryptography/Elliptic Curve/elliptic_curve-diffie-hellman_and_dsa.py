# elliptic-curve-diffie-hellman.py
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

# each party generates a private key
p_key1 =ec.generate_private_key(ec.SECP384R1())
p_key2 = ec.generate_private_key(ec.SECP384R1())

# exchange public keys
pub_key_1 = p_key1.public_key()
pub_key_2 = p_key2.public_key()

# each uses their private and the other's public key to derive shared secret
shared_key_1 = p_key1.exchange(ec.ECDH(), pub_key_2)
shared_key_2 = p_key2.exchange(ec.ECDH(), pub_key_1)

assert shared_key_1 == shared_key_2
print("Keys are the same")

# Elliptic Curve Digital Signature Algorithm (ECDSA)
# Signer creates signature using their private key, other's verify with signer's public key
private_key = ec.generate_private_key(ec.SECP384R1())
message = b"HELLO WORLD"
print(f"message: {message}")

# sign the message
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))
print(f"\nSigned message: {signature}")

# anyone can verify the signature with the public key
public_key = private_key.public_key()
try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print("\nSignature is valid!")
except:
    print("\nSignature is invalid!")

# If message is changed after signing, signature is invalid
message += b"MitM"
print(f"\nmessage: {message}")
try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print("\nSignature is valid!")
except:
    print("\nSignature is invalid!")
