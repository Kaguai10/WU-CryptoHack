Here you can encrypt in CBC but only decrypt in ECB. That shouldn't be a weakness because they're different modes... right?

Play at https://aes.cryptohack.org/ecbcbcwtf

## Challange


### Description

Here you can encrypt in CBC but only decrypt in ECB. That shouldn't be a weakness because they're different modes... right?

### HELP

This page offers a convenient way for you to interact with the challenge functions. You can also use GET requests to send and receive data directly from the listed routes/endpoints if you wish. For more information see the FAQ.

Your aim is to recover the `FLAG` value. Once you have it, submit it on the <a href='https://cryptohack.org/challenges/aes'>CryptoHack Symmetric Ciphers page</a>.

`Source`
```python
from Crypto.Cipher import AES


KEY = ?
FLAG = ?


@chal.route('/ecbcbcwtf/decrypt/<ciphertext>/')
def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


@chal.route('/ecbcbcwtf/encrypt_flag/')
def encrypt_flag():
    iv = os.urandom(16)

    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(FLAG.encode())
    ciphertext = iv.hex() + encrypted.hex()

    return {"ciphertext": ciphertext}
```

## Solve

`solver.py`
```python
import requests
from pwn import xor

BASE = "http://aes.cryptohack.org/ecbcbcwtf"

def get_json(path):
    return requests.get(f"{BASE}/{path}/").json()

def decrypt(block):
    return bytes.fromhex(get_json(f"decrypt/{block}")["plaintext"])

# Ambil ciphertext flag
ciphertext = get_json("encrypt_flag")["ciphertext"]

# Pecah per blok 16 byte = 32 hex char
blocks = [ciphertext[i:i+32] for i in range(0, len(ciphertext), 32)]

iv = blocks[0]
cipher_blocks = blocks[1:]

flag = b""

for prev, curr in zip(blocks, cipher_blocks):
    plaintext_block = xor(decrypt(curr), bytes.fromhex(prev))
    flag += plaintext_block

print(flag.decode())
```

Flag: `crypto{3cb_5uck5_4v01d_17_!!!!!}`
