I've encrypted the flag with my secret key, you'll never be able to guess it.

>Remember the flag format and how it might help you in this challenge!

`0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104`

## Solve
`find_key.py`
```python
cipher_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher = bytes.fromhex(cipher_hex)

known = b"crypto{"

key = bytes([c ^ k for c, k in zip(cipher[:len(known)], known)])
print("Key:", key)

plaintext = bytes([c ^ key[i % len(key)] for i, c in enumerate(cipher)])
print(plaintext.decode())
```

run => `python3 find_key.py`

```
output:
Key: b'myXORke'
crypto{%r~n-LQCnAUaY6ifjtJ▒JMvXeb_lGja
```

Disini bentuk string flagnya masih kurang jelas Tetapi kita sudah menemukan awalan key kita yaitu 'myXORke' kita asumsikan bahwa itu teks yang kurang satu huruf yaitu 'y', jadi kita coba untuk decode dengan key 'myXORkey'

`solver.py`
```python
cipher = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

key = b"myXORkey"

plaintext = bytes([c ^ key[i % len(key)] for i, c in enumerate(cipher)])
print(plaintext.decode())
```

run => `python3 solver.py`

Flag: `crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}`
