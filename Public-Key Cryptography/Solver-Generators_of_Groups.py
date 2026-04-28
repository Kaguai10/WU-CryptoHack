from sympy import isprime

p = 28151
factors = [2, 5, 563]

for g in range(2, p):
    ok = True
    for q in factors:
        if pow(g, (p-1)//q, p) == 1:
            ok = False
            break
    if ok:
        print("primitive root:", g)
        break
