from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from pwn import *
import json
from sympy.ntheory.residue_ntheory import discrete_log

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(len(padding)))

def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]

    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

# remote connection
r = remote('socket.cryptohack.org', 13379)

r.recvuntil(b"Send to Bob:")
r.sendline(b'{"supported": ["DH64"]}')

r.recvuntil(b"Send to Alice:")
r.sendline(b'{"chosen": "DH64"}')

r.recvuntil(b"Intercepted from Alice:")
data = json.loads(r.readline().decode())
p = int(data["p"], 16)
g = int(data["g"], 16)
A = int(data["A"], 16)

r.recvuntil(b"Intercepted from Bob:")
data = json.loads(r.readline().decode())
B = int(data["B"], 16)

r.recvuntil(b"Intercepted from Alice:")
data = json.loads(r.readline().decode())
iv = data["iv"]
ciphertext = data["encrypted_flag"]

# calculate a, b
a = discrete_log(p, A, g)
b = discrete_log(p, B, g)

print("The value of a and b", {a, b})

shared_secret = pow(B, a, p)
print("Shared_secret is: ", shared_secret)

print(decrypt_flag(shared_secret, iv, ciphertext))

r.close()

# Flag: crypto{d0wn6r4d35_4r3_d4n63r0u5}
