import math
from random import randint

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_candidate():
    while True:
        candidate = randint(2, 50)
        if is_prime(candidate):
            return candidate

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def mod_inverse(e, phi):
    g, x, y = extended_gcd(e, phi)
    if g != 1:
        raise Exception('No modular inverse')
    return x % phi

def encryption(key, data):
    e, n = key
    return pow(data, e, n)  # pow(data, e, n) is equivalent to (data ** e) % n

def decryption(key, data):
    d, n = key
    return pow(data, d, n)  # pow(data, d, n) is equivalent to (data ** d) % n

p = generate_prime_candidate()
q = generate_prime_candidate()

n = p * q
phi = (p - 1) * (q - 1)

e = randint(2, phi - 1)
while gcd(e, phi) != 1:
    e = randint(2, phi - 1)

d = mod_inverse(e, phi)

PU = (e, n) 
PR = (d, n) 

data = 5

encrypted_data = encryption(PU, data)
print("Encrypted:", encrypted_data)

decrypted_data = decryption(PR, encrypted_data)
print("Decrypted:", decrypted_data)

