 I've struggled to get PyCrypto's counter mode doing what I want, so I've turned ECB mode into CTR myself. My counter can go both upwards and downwards to throw off cryptanalysts! There's no chance they'll be able to read my picture.

Play at https://aes.cryptohack.org/bean_counter

## Challange


### Description

I've struggled to get PyCrypto's counter mode doing what I want, so I've turned ECB mode into CTR myself. My counter can go both upwards and downwards to throw off cryptanalysts! There's no chance they'll be able to read my picture.

### HELP

This page offers a convenient way for you to interact with the challenge functions. You can also use GET requests to send and receive data directly from the listed routes/endpoints if you wish. For more information see the FAQ.

Your aim is to recover the `FLAG` value. Once you have it, submit it on the <a href='https://cryptohack.org/challenges/aes'>CryptoHack Symmetric Ciphers page</a>.

`Source`
```python
from Crypto.Cipher import AES


KEY = ?


class StepUpCounter(object):
    def __init__(self, step_up=False):
        self.value = os.urandom(16).hex()
        self.step = 1
        self.stup = step_up

    def increment(self):
        if self.stup:
            self.newIV = hex(int(self.value, 16) + self.step)
        else:
            self.newIV = hex(int(self.value, 16) - self.stup)
        self.value = self.newIV[2:len(self.newIV)]
        return bytes.fromhex(self.value.zfill(32))

    def __repr__(self):
        self.increment()
        return self.value



@chal.route('/bean_counter/encrypt/')
def encrypt():
    cipher = AES.new(KEY, AES.MODE_ECB)
    ctr = StepUpCounter()

    out = []
    with open("challenge_files/bean_flag.png", 'rb') as f:
        block = f.read(16)
        while block:
            keystream = cipher.encrypt(ctr.increment())
            xored = [a^b for a, b in zip(block, keystream)]
            out.append(bytes(xored).hex())
            block = f.read(16)

    return {"encrypted": ''.join(out)}
```

## Solve

`solver.py`
```python
import requests
from itertools import cycle

URL = "http://aes.cryptohack.org/bean_counter/encrypt/"
PNG_HEADER = bytes.fromhex("89504e470d0a1a0a0000000d49484452")


def fetch_ciphertext():
    response = requests.get(URL)
    response.raise_for_status()
    return bytes.fromhex(response.json()["encrypted"])


def xor_bytes(data, key):
    return bytes(a ^ b for a, b in zip(data, cycle(key)))


def main():
    ciphertext = fetch_ciphertext()

    # Ambil keystream dari known plaintext PNG header
    keystream = bytes(
        c ^ p for c, p in zip(ciphertext[:len(PNG_HEADER)], PNG_HEADER)
    )

    plaintext = xor_bytes(ciphertext, keystream)

    with open("bean_counter.png", "wb") as f:
        f.write(plaintext)

    print("Saved as bean_counter.png")


if __name__ == "__main__":
    main()
```

Flag: `crypto{hex_bytes_beans}`
