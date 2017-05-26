import numpy as np


def inter(xe,x,y,n):
    A = np.zeros([n,n])
    A[:,n-1] = 1
    A[:,n-2] = x
    b = y
    for i in range(0,n-2)[::-1]:
        A[:,i] = np.multiply(A[:,i+1],x)
    c = gauss(A,b)
    D = Restos(n,c,xe)
    return c,D