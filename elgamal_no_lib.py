
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
