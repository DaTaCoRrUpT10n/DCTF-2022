import random

ciphertext = open('enc','rb').read()
for ad in range(256):
    for b in range(256):
        deciphered = b''
        for i in range(len(ciphertext)):
            deciphered+=((ad*(ciphertext[i]-b))%256).to_bytes(1,'big')
        if deciphered.__contains__(b"DCTF"):
            print(deciphered)
