ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.
Using the below integer array, convert the numbers to their corresponding ASCII characters to obtain a flag.

`[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]`

><strong>"In Python, the chr() function can be used to convert an ASCII ordinal number to a character (the ord() function does the opposite)."</strong>

Solve:
### `solver.py`
```python
#chr() => ascii to strings
#ord() => strings to ascii

ascii = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 95, 112, 144, 49, 110, 116, 52, 98, 108, 51, 125]
print("".join(chr(x) for x in ascii))
```
run => `python3 solver.py`

flag: `crypto{ASCI_p1nt4bl3}`
