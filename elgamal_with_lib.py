from elgamal.elgamal import Elgamal

# Declare Alice message, parsed to bytes
m = b'Hi Bob! How are you?'
print(m)

# Gets the public and private key, using 256 bits.
public_key, private_key = Elgamal.newkeys(256)

print("Public: {}".format(public_key))
print("Private: {}".format(private_key))

# Alice encrypts message with public key
ct = Elgamal.encrypt(m, public_key)
print("Alice encrypted message is ", ct)

# Alice send the message, and the private key is shared to Bob to decrypt the message
decrypted_message = Elgamal.decrypt(ct, private_key)

# Bob reads decrypted message
print("Bob reads: {}".format(decrypted_message.decode("utf-8") ))
