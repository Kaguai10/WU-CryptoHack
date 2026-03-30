For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.

I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

`73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d`

## Solve
`solver.py`
```python
a = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

key = a[0] ^ ord('c')
print("".join(chr(c ^ key) for c in a))
```

run => `python3 solver.py`

Flag: `crypto{0x10_15_my_f4v0ur173_by7e}`
