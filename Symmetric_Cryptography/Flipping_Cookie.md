 You can get a cookie for my website, but it won't help you read the flag... I think.

Play at https://aes.cryptohack.org/flipping_cookie

## Challange


### Description

You can get a cookie for my website, but it won't help you read the flag... I think.

### HELP

This page offers a convenient way for you to interact with the challenge functions. You can also use GET requests to send and receive data directly from the listed routes/endpoints if you wish. For more information see the FAQ.

Your aim is to recover the `FLAG` value. Once you have it, submit it on the <a href='https://cryptohack.org/challenges/aes'>CryptoHack Symmetric Ciphers page</a>.

`Source`
```python
from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta


KEY = ?
FLAG = ?


@chal.route('/flipping_cookie/check_admin/<cookie>/<iv>/')
def check_admin(cookie, iv):
    cookie = bytes.fromhex(cookie)
    iv = bytes.fromhex(iv)

    try:
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(cookie)
        unpadded = unpad(decrypted, 16)
    except ValueError as e:
        return {"error": str(e)}

    if b"admin=True" in unpadded.split(b";"):
        return {"flag": FLAG}
    else:
        return {"error": "Only admin can read the flag"}


@chal.route('/flipping_cookie/get_cookie/')
def get_cookie():
    expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
    cookie = f"admin=False;expiry={expires_at}".encode()

    iv = os.urandom(16)
    padded = pad(cookie, 16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(padded)
    ciphertext = iv.hex() + encrypted.hex()

    return {"cookie": ciphertext}
```

## Solve

`solver.py`
```python
import requests
from pwn import xor

BASE = "http://aes.cryptohack.org/flipping_cookie"


def get_cookie():
    r = requests.get(f"{BASE}/get_cookie/")
    return r.json()["cookie"]


def check_admin(cookie, iv):
    r = requests.get(f"{BASE}/check_admin/{cookie}/{iv}/")
    return r.json()


cookie = get_cookie()

iv = bytes.fromhex(cookie[:32])
ciphertext = cookie[32:]

original = b"admin=False"
target   = b"admin=True;"

new_iv = xor(iv, original, target)

result = check_admin(ciphertext, new_iv.hex())

print(result)
```

Flag: `crypto{4u7h3n71c4710n_15_3553n714l}`
