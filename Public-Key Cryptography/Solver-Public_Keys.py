# "Encrypt" the number 1212 using the exponent e=65537e=65537 and the primes p=17p=17 and q=23q=23. What number do you get as the ciphertext? 

n = 17 * 23
e = 65537

flag = pow(12, e, n)
print(flag)

# Flag: 301
