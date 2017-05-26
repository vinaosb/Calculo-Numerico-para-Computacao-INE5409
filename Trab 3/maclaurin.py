import numpy as np


def maclaurin(x,n):
    y = np.zeros(len(x))
    for i in range(1,n):
        y += (((-1)**(i+1))*(x**(2*i-1)))/fac(2*i - 1)
    return y
    
        
def fac(n):
    fac = 1.
    for i in range(1,n+1):
        fac *= (i)
    return fac