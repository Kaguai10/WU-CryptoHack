 We're going to skip over the finer details of the <b>KeyExpansion</b> phase for now. The main point is that it takes in our 16 byte key and produces 11 4x4 matrices called "round keys" derived from our initial key. These round keys allow AES to get extra mileage out of the single key that we provided.

The <b>initial key addition</b> phase, which is next, has a single AddRoundKey step. The AddRoundKey step is straightforward: it XORs the current state with the current round key.

<div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
  <img src="https://raw.githubusercontent.com/Kaguai10/CryptoHack/refs/heads/main/Symmetric_Cryptography/images/AddRoundKey.png">
</div>

<i>AddRoundKey</i> also occurs as the final step of each round. AddRoundKey is what makes AES a "keyed permutation" rather than just a permutation. It's the only part of AES where the key is mixed into the state, but is crucial for determining the permutation that occurs.

As you've seen in previous challenges, XOR is an easily invertible operation if you know the key, but tough to undo if you don't. Now imagine trying to recover plaintext which has been XOR'd with 11 different keys, and heavily jumbled between each XOR operation with a series of substitution and transposition ciphers. That's kinda what AES does! And we'll see just how effective the jumbling is in the next few challenges.

Complete the `add_round_key` function, then use the `matrix2bytes` function to get your next flag.

## Challange

```python
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    ???


print(add_round_key(state, round_key))
```

## Solver
`solver.py`
```python
#!/usr/bin/env python3

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    return [
        [s[i][j] ^ k[i][j] for j in range(4)]
        for i in range(4)
    ]


def matrix2bytes(matrix):
    # flatten row by row
    return bytes(sum(matrix, []))


def solve():
    result_matrix = add_round_key(state, round_key)
    
    print("[+] Matrix Result:")
    for row in result_matrix:
        print(row)
    
    flag = matrix2bytes(result_matrix).decode()
    print("\n[+] Flag:", flag)


if __name__ == "__main__":
    solve()
```

run => `python3 solver.py`

Flag: `crypto{r0undk3y}`
