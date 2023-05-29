#!python3

import numpy as np
import algo

def f(x):
    n = 19
    res = x**n * np.exp(-x)
    return res

a = -1.
b =  1.
p = 4

res = algo.quadTrap(a,b,p,f)

print("I20 = ",res)

I1 = res
I0 = 0.

exp = np.exp(1)
Invexp = 1 / exp

for i in range(20,0,-1) :
    I0 = (I1 + Invexp - (-1)**i * exp ) / i
    I1 = I0
    print("I"+str(i-1)+" = "+str(I0))
