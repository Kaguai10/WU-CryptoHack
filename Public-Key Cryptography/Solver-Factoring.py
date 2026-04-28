from sympy import factorint

n = 510143758735509025530880200653196460532653147

factors = factorint(n)

p, q = list(factors.keys())

print("p =", p)
print("q =", q)

# Flag: 19704762736204164635843

'''
http://factordb.com/index.php?query=510143758735509025530880200653196460532653147
'''
