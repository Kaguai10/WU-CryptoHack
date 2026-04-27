 Some block cipher modes, such as OFB, CTR, or CFB, turn a block cipher into a stream cipher. The idea behind stream ciphers is to produce a pseudorandom keystream which is then XORed with the plaintext. One advantage of stream ciphers is that they can work of plaintext of arbitrary length, with no padding required.

OFB is an obscure cipher mode, with no real benefits these days over using CTR. This challenge introduces an unusual property of OFB.

Play at https://aes.cryptohack.org/symmetry

## Challange


### Description

Some block cipher modes, such as OFB, CTR, or CFB, turn a block cipher into a stream cipher. The idea behind stream ciphers is to produce a pseudorandom keystream which is then XORed with the plaintext. One advantage of stream ciphers is that they can work of plaintext of arbitrary length, with no padding required.

OFB is an obscure cipher mode, with no real benefits these days over using CTR. This challenge introduces an unusual property of OFB.

### HELP

This page offers a convenient way for you to interact with the challenge functions. You can also use GET requests to send and receive data directly from the listed routes/endpoints if you wish. For more information see the FAQ.

Your aim is to recover the `FLAG` value. Once you have it, submit it on the <a href='https://cryptohack.org/challenges/aes'>CryptoHack Symmetric Ciphers page</a>.

`Source`
```python
from Crypto.Cipher import AES


KEY = ?
FLAG = ?


@chal.route('/symmetry/encrypt/<plaintext>/<iv>/')
def encrypt(plaintext, iv):
    plaintext = bytes.fromhex(plaintext)
    iv = bytes.fromhex(iv)
    if len(iv) != 16:
        return {"error": "IV length must be 16"}

    cipher = AES.new(KEY, AES.MODE_OFB, iv)
    encrypted = cipher.encrypt(plaintext)
    ciphertext = encrypted.hex()

    return {"ciphertext": ciphertext}


@chal.route('/symmetry/encrypt_flag/')
def encrypt_flag():
    iv = os.urandom(16)

    cipher = AES.new(KEY, AES.MODE_OFB, iv)
    encrypted = cipher.encrypt(FLAG.encode())
    ciphertext = iv.hex() + encrypted.hex()

    return {"ciphertext": ciphertext}
```

## Solve

`solver.py`
```python
import requests

BASE = "http://aes.cryptohack.org/symmetry"

def encrypt(plaintext, iv):
    r = requests.get(f"{BASE}/encrypt/{plaintext}/{iv}/")
    return bytes.fromhex(r.json()["ciphertext"])

def get_flag():
    r = requests.get(f"{BASE}/encrypt_flag/")
    return r.json()["ciphertext"]

data = get_flag()

iv = data[:32]
ciphertext = bytes.fromhex(data[32:])

zeros = "00" * len(ciphertext)
keystream = encrypt(zeros, iv)

flag = bytes(c ^ k for c, k in zip(ciphertext, keystream))

print(flag.decode())
```

Flag: `crypto{0fb_15_5ymm37r1c4l_!!!11!}`
