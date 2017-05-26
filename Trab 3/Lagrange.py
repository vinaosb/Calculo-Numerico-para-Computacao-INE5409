import numpy as np

def L(i, a, x):
    n = len(a)
    num = 1.
    den = 1.
    for j in range(0,n):
        if j != i:
            num = (x - a[j])*num
            den = (a[i] - a[j])*den
    l = (num/den)
    return l

def P(x,a,b):
    n = len(a)
    p = 0.0
    for i in range(0,n):
        p = p + b[i]*L(i,a,x)
    return p