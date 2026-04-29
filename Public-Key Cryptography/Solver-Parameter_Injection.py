from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib, json
from pwn import *

def decrypt_flag(shared_secret, iv, ciphertext):
    key = hashlib.sha1(str(shared_secret).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_CBC, bytes.fromhex(iv))
    plaintext = cipher.decrypt(bytes.fromhex(ciphertext))

    try:
        return unpad(plaintext, 16).decode()
    except:
        return plaintext.decode()

p = remote('socket.cryptohack.org', 13371)

p.recvuntil(b"Send to Bob:")
p.sendline(b'{"p":"0x01","g":"0x02","A":"0x03"}')

p.recvuntil(b"Intercepted from Bob:")
p.sendline(b'{"B":"0x01"}')

p.recvuntil(b"Intercepted from Alice:")
data = json.loads(p.readline())

print(decrypt_flag(1, data["iv"], data["encrypted_flag"]))

# Flag: crypto{n1c3_0n3_m4ll0ry!!!!!!!!}
