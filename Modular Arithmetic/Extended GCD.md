Let a and b be positive integers.

The extended Euclidean algorithm is an efficient way to find integers u,v such that

`a⋅u+b⋅v=gcd⁡(a,b)`

><strong>Later, when we learn to decrypt RSA ciphertexts, we will need this algorithm to calculate the modular inverse of the public exponent.</strong>

Using the two primes `p=26513,q=32321` find the integers u,v such that

`p⋅u+q⋅v=gcd⁡(p,q)`

Enter whichever of u and v is the lower number as the flag.

><strong>Knowing that p,q are prime, what would you expect gcd⁡(p,q) to be? For more details on the extended Euclidean algorithm, check out <a href=https://web.archive.org/web/20230511143526/http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html> this page.<a></strong>

## Solver
`solver.py`
```python
def extended_gcd(p,q):
    if p == 0:
        return (q, 0, 1)
    else:
        (gcd, u, v) = extended_gcd(q % p, p)
        return (gcd, v - (q // p) * u, u)

p = 26513
q = 32321

gcd, u, v = extended_gcd(p, q)
print("[+] GCD: {}".format(gcd))
print("[+] u,v: {},{}".format(u,v))
print("\n[*] FLAG: crypto{{{},{}}}".format(u,v))
```

run => `python3 solver.py`

Flag: crypto{10245,-8404}
