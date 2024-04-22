# Crypto Hashing in Python using SHA-256
# As part of: https://learning.quantum.ibm.com/course/practical-introduction-to-quantum-safe-cryptography/cryptographic-hash-functions

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

# Return no. of chars different in two strings
def char_diff(str1, str2):
    return sum(str1[i] != str2[i] for i in range(len(str1)))

# Messages to be hashed - differ by one char
msg_1 = b"Buy 100000 shares of WXYZ stock today!"
msg_2 = b"Buy 100000 shares of VXYZ stock today!"
print(f"The messages differ by {char_diff(msg_1, msg_2)} chars.\n\n")

"""
Due to avalanche effect in SHA-256 CHF, one char difference in messages
will produce two very different digests.
"""

# Create SHA-256 hash object for each message
chf_1 = hashes.Hash(hashes.SHA256(), backend=default_backend())
chf_2 = hashes.Hash(hashes.SHA256(), backend=default_backend())

# Update each hash object with bytes of messages
chf_1.update(msg_1)
chf_2.update(msg_2)

# Finalize hash process, obtain digests
dig_1 = chf_1.finalize()
dig_2 = chf_2.finalize()

# Convert resulting hashes to hex strings for convenient printing
dig_1_str = dig_1.hex()
dig_2_str = dig_2.hex()

# Print out the digests as strings
print(f"Digest-1: {dig_1_str}")
print(f"Digest-2: {dig_2_str}")
print(f"The digests differ by {char_diff(dig_1_str, dig_2_str)} characters.")
