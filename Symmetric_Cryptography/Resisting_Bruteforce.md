If a block cipher is secure, there should be no way for an attacker to distinguish the output of AES from a random permutation of bits. Furthermore, there should be no better way to undo the permutation than simply bruteforcing every possible key. That's why academics consider a cipher theoretically "broken" if they can find an attack that takes fewer steps to perform than bruteforcing the key, even if that attack is practically infeasible.

><strong>How difficult is it to bruteforce a 128-bit keyspace? Somebody estimated that if you turned the power of the entire Bitcoin mining network against an AES-128 key, it would take over a hundred times the age of the universe to crack the key.</strong>

It turns out that there is an attack on AES that's better than bruteforce, but only slightly – it lowers the security level of AES-128 down to 126.1 bits, and hasn't been improved on for over 8 years. Given the large "security margin" provided by 128 bits, and the lack of improvements despite extensive study, it's not considered a credible risk to the security of AES. But yes, in a very narrow sense, it "breaks" AES.

Finally, while quantum computers have the potential to completely break popular public-key cryptosystems like RSA via Shor's algorithm, they are thought to only cut in half the security level of symmetric cryptosystems via Grover's algorithm. This is one reason why people recommend using AES-256, despite it being less performant, as it would still provide a very adequate 128 bits of security in a quantum future.

What is the name for the best single-key attack against AES? 

## Solve

A biclique attack is a variant of the meet-in-the-middle (MITM) method of cryptanalysis. It utilizes a biclique structure to extend the number of possibly attacked rounds by the MITM attack. Since biclique cryptanalysis is based on MITM attacks, it is applicable to both block ciphers and (iterated) hash-functions. Biclique attacks are known for having weakened both full AES and full IDEA,though only with slight advantage over brute force. It has also been applied to the KASUMI cipher and preimage resistance of the Skein-512 and SHA-2 hash functions. <a href=https://en.wikipedia.org/wiki/Biclique_attack>read more</a>

Flag: crypto{biclique}
