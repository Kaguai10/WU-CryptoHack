ECB is the most simple mode, with each plaintext block encrypted entirely independently. In this case, your input is prepended to the secret flag and encrypted and that's it. We don't even provide a decrypt function. Perhaps you don't need a padding oracle when you have an "ECB oracle"?

Play at https://aes.cryptohack.org/ecb_oracle

## Challange


### DESCRIPTION

It is essential that keys in symmetric-key algorithms are random bytes, instead of passwords or other predictable data. The random bytes should be generated using a cryptographically-secure pseudorandom number generator (CSPRNG). If the keys are predictable in any way, then the security level of the cipher is reduced and it may be possible for an attacker who gets access to the ciphertext to decrypt it.

Just because a key looks like it is formed of random bytes, does not mean that it necessarily is. In this case the key has been derived from a simple password using a hashing function, which makes the ciphertext crackable.

For this challenge you may script your HTTP requests to the endpoints, or alternatively attack the ciphertext offline. Good luck!

### HELP

This page offers a convenient way for you to interact with the challenge functions. You can also use GET requests to send and receive data directly from the listed routes/endpoints if you wish. For more information see the FAQ.

Your aim is to recover the `FLAG` value. Once you have it, submit it on the <a href='https://cryptohack.org/challenges/aes'>CryptoHack Symmetric Ciphers page</a>.

`Source`
```python
from Crypto.Cipher import AES
from Crypto.Cipher import AES
import hashlib
import random


# /usr/share/dict/words from
# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words
with open("/usr/share/dict/words") as f:
    words = [w.strip() for w in f.readlines()]
keyword = random.choice(words)

KEY = hashlib.md5(keyword.encode()).digest()
FLAG = ?


@chal.route('/passwords_as_keys/decrypt/<ciphertext>/<password_hash>/')
def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


@chal.route('/passwords_as_keys/encrypt_flag/')
def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return {"ciphertext": encrypted.hex()}
```

## Solve

1. **Send input to the server**
   The server encrypts:

   ```
   your_input + FLAG
   ```

2. **Exploit ECB weakness**
   In AES-ECB:

   ```
   same plaintext block → same ciphertext block
   ```

3. **Control the input length**

   Send many `a` characters so:

   * the flag aligns at the end of a block

4. **Guess one character**

   Try all possible characters:

   ```
   aaaaa... + guess
   ```

5. **Compare ciphertext blocks**

   If two blocks are equal:

   * your guess is correct

6. **Save the correct character**

   Build the flag step by step:

   ```
   c → cr → cry → ...
   ```

7. **Shift and repeat**

   Repeat the process until the full flag is recovered


`solver.py`
```python
import requests
import string

url = "https://aes.cryptohack.org/ecb_oracle/encrypt/"
chars = string.printable

s0 = "a" * 16
s1 = "a" * 16
flag = ""
last = ""

session = requests.Session()

for i in range(31):
    s1 = s1[1:] + last
    pad = "a" * (31 - i)

    for ch in chars:
        payload = (s0 + s1 + ch + pad).encode().hex()
        r = session.get(url + payload + "/").json()

        ct = bytes.fromhex(r["ciphertext"])

        if ct[16:32] == ct[48:64]:
            flag += ch
            last = ch
            print(flag)

            if ch == "}":
                print("[+] Flag found:", flag)
                exit()

            break
```

Flag: `crypto{p3n6u1n5_h473_3cb}`
