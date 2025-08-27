import random
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()
random.shuffle(key)

msg = input("Enter a message to encrypt: ")
enc_msg = ""

#encrypt
for ltr in msg:
    index = chars.index(ltr)
    enc_msg += (key[index])

print(f"The original message: {msg}")
print(f"The encrypted message: {enc_msg}")

#Decrypt
dec_msg = input("Enter a message to decrypt: ")
msg = ""

for ltr in dec_msg:
    index = key.index(ltr)
    msg += (chars[index])
print(f"The encrypted message: {enc_msg}")
print(f"The original message: {msg}")