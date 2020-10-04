print("Bob generates the following numbers and sends them to Alice as a public key")

print("q", public_key[0])
print("g", public_key[1])
print("h", public_key[2])

print("Now Alice can encrypt messages for Bob")

print("\n")
print("-"*20) 
print("Alice side")
print("-"*20) 
msg = "Hi Bob! How are you?"
print("Alice's message: ", msg)
en_msg, p = encrypt(msg, q, h, g) 
print("Alice sends the following encrypted message: ", en_msg)
print("With this value which is necessary for decrypt:", p)

print("\n")
print("-"*20) 
print("Bob's side")   
print("-"*20) 

dr_msg = decrypt(en_msg, p, a, q) 
dmsg = ''.join(dr_msg) 
print("Decrypted Message :", dmsg); 
