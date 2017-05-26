import numpy as np



def Simpson(n,a,b):
    h = (b-a)/n
    x = np.linspace(a,b,n+1)
    y = fx1(x)
    Sn = 0
    for i in range(1,n)[::2]:
        Sn += ((h*(y[i-1] + 4*y[i] + y[i+1]))/3)
    return Sn