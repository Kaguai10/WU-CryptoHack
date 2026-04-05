AES, like all good block ciphers, performs a "keyed permutation". This means that it maps every possible input block to a unique output block, with a key determining which permutation to perform.

><strong>A "block" just refers to a fixed number of bits or bytes, which may represent any kind of data. AES processes a block and outputs another block. We'll be specifically talking the variant of AES which works on 128 bit (16 byte) blocks and a 128 bit key, known as AES-128.</strong>

Using the same key, the permutation can be performed in reverse, mapping the output block back to the original input block. It is important that there is a one-to-one correspondence between input and output blocks, otherwise we wouldn't be able to rely on the ciphertext to decrypt back to the same plaintext we started with.

What is the mathematical term for a one-to-one correspondence? 

## Solve

In mathematics, bijection, bijective function, one-to-one correspondence, or reverse function is a function that involves elements of two sets. Each element of a set is precisely paired to one element from the other set. Each element of the other set is paired precisely to one element of the first set. There are no elements that are unpaired or have more than one pair. In mathematical terms, the bijective function f: X → Y is one-to-one mapping (injection) and onto (surjective) of the set X to the Y set.The term one-to-one correspondence should not be misinterpreted by the one-to-one function (injection function). <a href=https://en.wikipedia.org/wiki/Bijection>read more</a>

Flag: `crypto{bijection}`
