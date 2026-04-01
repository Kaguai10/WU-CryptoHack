The Chinese Remainder Theorem gives a unique solution to a set of linear congruences if their moduli are coprime.

This means, that given a set of arbitrary integers a<sup>i</sup>, and pairwise coprime integers n<sup>i</sup>, such that the following linear congruences hold:

><strong>Note "pairwise coprime integers" means that if we have a set of integers {n<sup>1</sup>,n<sup>2</sup>,...,n<sup>i</sup>}, all pairs of integers selected from the set are coprime: gcd⁡( n<sup>i</sup>, n<sup>j</sup> ) = 1.</strong>

```txt
x ≡ a¹ mod  n¹
x ≡ a² mod  n²
……
```

There is a unique solution x ≡ a mod  N where N = n<sup>1</sup>⋅n<sup>2</sup>⋅...⋅n<sup>n</sup>.

In cryptography, we commonly use the Chinese Remainder Theorem to help us reduce a problem of very large integers into a set of several, easier problems.

Given the following set of linear congruences:

```txt
x ≡ 2 mod  5
x ≡ 3 mod  11
x ≡ 5 mod  17
```

Find the integer aa such that `x ≡ a mod  935`.

><strong>Starting with the congruence with the largest modulus, use that for `x ≡ a mod p` we can write `x=a+k⋅p` for arbitrary integer k.</strong>

## Solve
`solver.py`
```python
from sympy.ntheory.modular import crt

n = [5, 11, 17]
a = [2, 3, 5]

print(crt(n, a)[0])
```

run => `python3 solver.py`

Flag: `872`
