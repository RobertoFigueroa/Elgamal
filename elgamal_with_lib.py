from elgamal.elgamal import Elgamal

# Declare Alice message, parsed to bytes
m = b'Hi Bob! How are you?'
print(m)

# Gets the public and private key, using 256 bits.
public_key, private_key = Elgamal.newkeys(256)

print("Public: {}".format(public_key))
print("Private: {}".format(private_key))
