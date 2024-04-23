# RSA Key Gen.py

""" GCD """
# Compute gcd, to test whether two integers are coprime
def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)
    
# examples
n1=gcd(50,10)
n2=gcd(99,33)
n3=gcd(59,9)

# same with math.gcd
import math
m1=math.gcd(50,10)
m2=math.gcd(99,33)
m3=math.gcd(59,9)

# confirm they're the same
assert(n1==m1)
assert(n2==m2)
assert(n3==m3)

# print
print("gcd(50,10) =", m1)
print("gcd(99,33) =", m2)
print("gcd(59,9) =", m3)


""" RSA Key Gen """
# Example secret prime numbers
p = 13
q = 19

# Calculate product (modulus) of the primes, this will part of public key 
# NOTE: real-world RSA uses a modulus n that is greater, e.g. 2048-bits long or 617 decimal digits
n = p*q
print("\nModulus n (p*q)=", n)

# Compute Euler totient phi(n) and keep it secret - Needed for modular multiplicative inverse operation to determine RSA keys
phi = (p-1) * (q-1)
print("Secret Euler Totient [phi(n)]:", phi)

# Calculating public key - RSA keys are specified by a tuple of two integers.; first is specific integer, second is modulus common to both keys. 

# integer e such that e and phi(n) are coprime
e = 2
while(e < phi):
    if (math.gcd(e, phi)==1):
        break
    else:
        e += 1
print("\nPublic Key (e):", e)

# value d such that (d*e) % phi(n) = 1 (multiplicative invers of e % phi) - satisfies congruency relation d∗e≡1(modφ(n))
# NOTE: Here we simply loop over positive integers to find d, in reality the extended Euclidian algorithm is used.
d = 1
while(True):
    if((d*e) % phi == 1):
        break
    else:
        d += 1
print("Private Key (d):", d)

# Gen the public & private key pair
public = (e, n)
private = (d, n)
print(f"\nPublic Key: {public}\nPrivate Key: {private}")


""" Encryption and Decryption Example 
In RSA, bot operations use modular exponentiation operation
Public and private keys are complementary, either can be used to encrypt message that the other can decrypt
Here we encrypt with public key (e,n) and decrypt with private (d,n) """
# Encryption
def encrypt(plain_text):
    return (plain_text ** e) % n

# Decryption
def decrypt(cipher_text):
    return (cipher_text ** d) % n

# Message to encode
msg = 69

enc_msg = encrypt(msg)
dec_msg = decrypt(enc_msg)

print("\nOriginal message:", msg)
print("Encrypted message:", enc_msg)
print("Decrypted message:", dec_msg)
