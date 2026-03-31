We'll pick up from the last challenge and imagine we've picked a modulus p, and we will restrict ourselves to the case when p is prime.

The integers modulo `p` define a field, denoted F<sub>p</sub>​.

><strong>If the modulus is not prime, the set of integers modulo n define a ring.</strong>

A finite field F<sub>p​</sub> is the set of integers `0,1,...,p−1`, and under both addition and multiplication there are inverse elements `b+`​ and `b∗`​ for every element a in the set, such that `a+b+=0` and `a⋅b∗=1`.

><strong>Note that the identity element for addition and multiplication is different! This is because the identity when acted with the operator should do nothing: `a+0=a` and `a⋅1=a`.</strong>

Lets say we pick `p=17`. Calculate 3<sup>17</sup> mod  17. Now do the same but with 5<sup>17</sup> mod  17.

What would you expect to get for 7<sup>16</sup> mod  17? Try calculating that.

This interesting fact is known as Fermat's little theorem. We'll be needing this (and its generalisations) when we look at RSA cryptography.

Now take the prime p=65537. Calculate 273246787654<sup>65536</sup> mod  65537.

Did you need a calculator? 

## Solve
`solver.py`
```python
p = 65537
a = 273246787654
power = 65536

print(pow(a, power, p))
```

run => `python3 solver.py`

Flag: `1`
