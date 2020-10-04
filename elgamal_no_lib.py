#Reference https://www.geeksforgeeks.org/elgamal-encryption-algorithm/

import random
from math import gcd

#returns a number that is coprime with q
def gen_key(q): 
    key = random.randint(300, q) 
    while gcd(q, key) != 1: 
        key = random.randint(300, q) 
    return key 

# Modular exponentiation 
def power(a, b, c): 
    x = 1
    y = a 
  
    while b > 0: 
        if b % 2 == 0: 
            x = (x * y) % c; 
        y = (y * y) % c 
        b = int(b / 2) 
  
    return x % c 

# Modular exponentiation 
def power(a, b, c): 
    x = 1
    y = a 
  
    while b > 0: 
        if b % 2 == 0: 
            x = (x * y) % c; 
        y = (y * y) % c 
        b = int(b / 2) 
  
    return x % c 

# Asymmetric encryption 
def encrypt(msg, q, h, g): 
  
    en_msg = [] 
  
    k = gen_key(q)# Private key for sender 
    s = power(h, k, q) 
    p = power(g, k, q) 
      
    for i in range(0, len(msg)): 
        en_msg.append(msg[i]) 
  
    for i in range(0, len(en_msg)): 
        en_msg[i] = s * ord(en_msg[i]) 
  
    return en_msg, p 

def decrypt(en_msg, p, key, q): 
  
    dr_msg = [] 
    h = power(p, key, q) 
    for i in range(0, len(en_msg)): 
        dr_msg.append(chr(int(en_msg[i]/h))) 
          
    return dr_msg


print("-"*20) 
print("Bob's side")   
print("-"*20) 
#generate random prime number
q = random.randint(pow(10, 20), pow(10, 50)) 
#generate g
g = random.randint(2, q)
#generate a that has to be coprime with q (this is my secrete key)
a = gen_key(q)
#generate h
h = power(g, a, q)
#We send to Alice [q, g, h] which is my public key
public_key = [q, g, h]
