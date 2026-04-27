The previous set of challenges showed how AES performs a keyed permutation on a block of data. In practice, we need to encrypt messages much longer than a single block. A mode of operation describes how to use a cipher like AES on longer messages.

All modes have serious weaknesses when used incorrectly. The challenges in this category take you to a different section of the website where you can interact with APIs and exploit those weaknesses. Get yourself acquainted with the interface and use it to take your next flag!

Play at https://aes.cryptohack.org/block_cipher_starter

## Challange


### Description

The previous set of challenges showed how AES performs a keyed permutation on a block of data. In practice, we need to encrypt messages much longer than a single block. A mode of operation describes how to use a cipher like AES on longer messages.

All modes have serious weaknesses when used incorrectly. The challenges in this category take you to a different section of the website where you can interact with APIs and exploit those weaknesses. Get yourself acquainted with the interface and use it to take your next flag!

### Help

This page offers a convenient way for you to interact with the challenge functions. You can also use GET requests to send and receive data directly from the listed routes/endpoints if you wish. For more information see the FAQ.

Your aim is to recover the `FLAG` value. Once you have it, submit it on the <a href='https://cryptohack.org/challenges/aes'>CryptoHack Symmetric Ciphers page.</a>

`Source`
```python
from Crypto.Cipher import AES


KEY = ?
FLAG = ?


@chal.route('/block_cipher_starter/decrypt/<ciphertext>/')
def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


@chal.route('/block_cipher_starter/encrypt_flag/')
def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return {"ciphertext": encrypted.hex()}
```

## Solve

*Solution Steps*

1. **Encrypt the Flag**
   Click the **`Encrypt_Flag()`** button.
   The system will generate the following ciphertext:

   ```
   a1043d8f29cb53244860394631aa38f9ae1f8f8fba26f39fa6bed02ee4fa595d
   ```

2. **Decrypt the Ciphertext**
   Copy the ciphertext obtained from the encryption step, then paste it into the **`Decrypt(CIPHERTEXT)`** field and submit it.
   The resulting decrypted output will be:

   ```
   63727970746f7b626c30636b5f633170683372355f3472335f663435375f217d
   ```

3. **Decode the Hexadecimal Output**
   Take the decrypted result (which is in hexadecimal format) and input it into the **Hex Decoder** under *“Enter Hex Here”*:

   ```
   63727970746f7b626c30636b5f633170683372355f3472335f663435375f217d
   ```

5. **Retrieve the Flag**
   After decoding the hexadecimal string, the final flag is obtained:

   ```
   crypto{bl0ck_c1ph3r5_4r3_f457_!}
   ```

**Versi menggunakan skrip python**
`solver.py`

```python
#!/usr/bin/env python3
import requests

BASE_URL = "https://aes.cryptohack.org/block_cipher_starter"


def request_json(endpoint):
    url = f"{BASE_URL}/{endpoint}/"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def get_encrypted_flag():
    data = request_json("encrypt_flag")
    return data["ciphertext"]


def decrypt_ciphertext(ciphertext):
    data = request_json(f"decrypt/{ciphertext}")
    return data["plaintext"]


def hex_to_text(hex_string):
    return bytes.fromhex(hex_string).decode()


def main():
    encrypted_flag = get_encrypted_flag()
    decrypted_hex = decrypt_ciphertext(encrypted_flag)
    flag = hex_to_text(decrypted_hex)

    print("[+] Encrypted Flag:")
    print(encrypted_flag)

    print("\n[+] Decrypted Hex:")
    print(decrypted_hex)

    print("\n[+] Flag:")
    print(flag)


if __name__ == "__main__":
    main()

```
