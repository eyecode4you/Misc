# discrete_logarithm_problem.py
# a^e mod M = c
# Find a given only e, M, and c

# Generate elements of (Z_7)^{x} using generator [5].
g=5
p=7 # reduction modulo
print(f"Using generator {g}")
# k used for exponentioation
for k in range(3*p):
    print(f"{g}**{k} mod {p} = {(g**k)%7}")

# cycle repeates indefinitely with a period p - 1 = 6