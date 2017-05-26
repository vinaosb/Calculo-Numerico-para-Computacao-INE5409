import numpy as np


def inter(x,y,n):
    A = np.zeros([n,n])
    b = np.zeros(n)
    for i in range(0,n):
        A[i,n-1] = 1.
        for j in range(0,n-1)[::-1]:
            A[i,j] = A[i,j+1]*x[i]
        b[i] = y[i]
    b = gauss(A,b)
    D = Restos(n,b,x[1])
    return D