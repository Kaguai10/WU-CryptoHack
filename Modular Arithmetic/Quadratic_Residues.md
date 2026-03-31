We've looked at multiplication and division in modular arithmetic, but what does it mean to take the square root modulo an integer?

For the following discussion, let's work modulo p=29. We can take the integer a=11 and calculate a<sup>2</sup> = 5 mod  29.

As a = 11,a<sup>2</sup> = 5, we say the square root of 5 is 11.

This feels good, but now let's think about the square root of 18. From the above, we know we need to find some integer a such that a<sup>2</sup> = 18

Your first idea might be to start with a=1 and loop to a=p−1. In this discussion p isn't too large and we can quickly check all options.

Have a go, try coding this and see what you find. If you've coded it right, you'll find that for all a∈F*<sub>p</sub> you never find an aa such that a2=18a2=18.

What we are seeing, is that for the elements of F*<sub>p</sub>​, not every element has a square root. In fact, what we find is that for roughly one half of the elements of F*<sub>p</sub>, there is no square root.

><strong>We say that an integer x is a Quadratic Residue if there exists an a such that a<sup>2</sup> ≡ x mod  p. If there is no such solution, then the integer is a Quadratic Non-Residue.</strong>

In other words, x is a quadratic residue when it is possible to take the square root of x modulo an integer p.

In the below list there are two non-quadratic residues and one quadratic residue.

Find the quadratic residue and then calculate its square root. Of the two possible roots, submit the smaller one as the flag.

><strong>If a<sup>2</sup> = x then (−a)<sup>2</sup> = x. So if x is a quadratic residue in some finite field, then there are always two solutions for a.</strong>

```txt
                                   p = 29      ints = [14,6,11]
```

## Solve
`solver.py`
```python
p = 29
result = []

for a in range(p):
    if (a * a) % p in [14, 6, 11]:
        result.append(a)

print(min(result))
```

run => `python3 solver.py`

Flag: 8
