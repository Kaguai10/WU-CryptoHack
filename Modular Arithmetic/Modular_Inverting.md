As we've seen, we can work within a finite field F<sub>p</sub>, adding and multiplying elements, and always obtain another element of the field.

For all elements g in the field, there exists a unique integer d such that `g⋅d ≡ 1 mod  p`.

This is the multiplicative inverse of `g`.

Example: `7⋅8 = 56 ≡ 1 mod  11`

What is the inverse element: d = 3<sup>−1</sup> such that `3⋅d ≡ 1 mod  13`?

><strong>Think about the little theorem we just worked with. How does this help you find the inverse of an element?</strong>

## Solve
`solver.py`
```python
from Crypto.Util.number import inverse
inverse(3, 13)
```

run => `python3 solver.py`

Flag: `9`
