""" breaking_rsa.py
Finding RSA private key given only the public key with brute force
e.g. we have a public key (5, 247)"""
import math

n = 247 # the modulus
e = 5 # public key no.
a = 6 # a selected coprime to n

# 1: Pick a number coprime to modulus, almost any guessed will do, here we use 6
assert math.gcd(a, n) == 1
print(f"Checked {n} and {a} are coprime")

# 2: Find period (interval at which function repeats itself) r such that 6^r ≡ 1(mod 247)
# we compute r classically using brute force - we could use Shor's algorithm on a quantum computer using Qiskit
r = 0
rem = 100
while(rem != 1):
    r += 1
    rem = (a**r) % n

print(f"Period r is: {r}")
assert a**r % n == 1

print(f"Checked {a}^{r} mod {n} is 1")

# 3: Since r=36 is even, we can compute f1=(a^r/2 −1),f2=(a^r/2 +1).
f1 = int (a**(r/2) - 1)
f2 = int (a**(r/2) + 1)

print(f"\nf1 = {f1}")
print(f"f2 = {f2}")

# 4: Find GCD of either of those factors with 𝑛. Divide 𝑛 with the prime factor already found to obtain the second prime factor.
q_found = math.gcd(f1, n)
print(f"\nOne possible prime factor of n ({n}) is: {q_found}")

# explicit int to avoid floating point
p_found = int (n/q_found)
print(f"The second prime factor of n ({n}) is: {p_found}")

assert n == p_found * q_found

# 5: On recovering the prime factors of n=247 as p_found=13 and q_found=19, we compute the totient ϕfound =(p_found −1)∗(q_found −1)
phi_found = (p_found-1) * (q_found-1)
print(f"\nTotient is: {phi_found}")

# Recover private key number d_found by satisfying (d_found * e) % phi_found = 1
d_found = 1
while(True):
    if ((d_found*e) % phi_found == 1):
        break
    else:
        d_found += 1
print("Private key number:", d_found)
