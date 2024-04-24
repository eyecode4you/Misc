# digital_signature_rsa.py
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed
from os import urandom

# Generate keys for Bob
bob_private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
bob_public_key = bob_private_key.public_key()
# Generate keys for Alice
alice_private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
alice_public_key = alice_private_key.public_key()
print("\nPrivate and Public keys generated for Bob and Alice.\n\n")

""" KDF & SYMMETRIC KEY EXCHANGE OPERATION """
# Alice generates a long secret from which the shared secret will be derived
alice_long_secret = urandom(160) # 160-byte (1280-bit) random message
print("Alice's secret created!")

# Alice encrypts secret using Bob's public key, sent to Bob
alice_encrypted_secret = bob_public_key.encrypt(
    alice_long_secret,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Alice's secret encrypted!")

# Bob decrypts secret using his private key
bob_decrypted_secret = bob_private_key.decrypt(
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
symmetric_key = symmetric_key_alice
print(f"\nA symmetric key of length {len(symmetric_key_alice)*8} bits was successfully derived by both Alice and Bob!")

""" DIGITAL SIGNATURE OPERATION 
1: Alice encrypts plaintext using Bob's public key
2: Alice creates hash of ciphertext and further encrypts with her private key - this encrypted hash is the signature
3: Alice transmits this to Bob
4: Bob uses Alice's public key to decrypt signature, revealing hashed ciphertext
5: Bob uses same hash function used by Alice to recreate a second instance 
    of the hashed ciphertext. If it matches the one sent by Alice, 
    message is validated
6: Bob decrypts the ciphertext using his own private key"""

# Alice encrypts the message using Bob's public key
ciphertext = bob_public_key.encrypt(
    symmetric_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("\nciphertext of symmetric key:",ciphertext)
""" Alice signs ciphertext using her private key
    1:Create hash of ciphertext
    2:Encrypt hash using Alice's private key """
digest = hashes.Hash(hashes.SHA256())
digest.update(ciphertext)
hash_to_sign = digest.finalize()

signature = alice_private_key.sign(
    hash_to_sign,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    Prehashed(hashes.SHA256())
)
print("\n\nAlice Signature: ", signature)

# Alice would then send ciphertext over network to Bob
received_ciphertext = ciphertext
received_signature = signature
print("\nSending ciphertext and signature to Bob...")

# Bob receives and verifies the ciphertext.
digest = hashes.Hash(hashes.SHA256())
digest.update(received_ciphertext)
hash_to_verify = digest.finalize()
print("\nhash to verify: ",hash_to_verify)

# Bob verifies signature using Alice's public key
try:
    alice_public_key.verify(
        received_signature,
        hash_to_verify,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        Prehashed(hashes.SHA256())
    )
    print("Signature is valid.")
except:
    print("Signature is not valid!")

# When verified, Bob can decrypt ciphertext using his private key as Alice encrypted it using his public key
decrypted_message = bob_private_key.decrypt(
    received_ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("\nDecrypted message (Symmetric Key):", decrypted_message)
print("Original Message                 :", symmetric_key)
assert decrypted_message == symmetric_key, "Symmetric Key Does Not Match!"
print("Symmetric Keys Match!")
