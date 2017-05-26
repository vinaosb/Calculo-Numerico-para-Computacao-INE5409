import numpy as np


def PolLegendre(m):
    n = m
    m += 2
    a = np.zeros([m,m+1])
    t = np.zeros([m,m])
    C = np.zeros([n,n])
    a[0,0] = 1
    a[1,0] = 3/2
    a[1,2] = -1/2
    for i in range(1,m-1):
        for j in range(0,m-1):
            a[i+1,j] += (2*(i+1)+1)*a[i,j]/(i+2)
            a[i+1,j+2] += - (i+1)*a[i-1,j]/(i+2)
    for i in range(0,m):
        t[i] = calcT(a[i])
        #t[0,0] = 1
    t = t[0:n,0:n]
    for i in range(0,n)[::2]:
        t[i] = np.sort(t[i])
        for j in range(0,n):
            count = 0
            for k in range(0,n-1):
                if (t[i,k] == 0 and count == 1):
                    t[i,k] = t[i,k+1]
                    t[i,k+1] = 0
                if (t[i,k] == 0 and count < 1):
                    count += 1
    for i in range(1,n)[::2]:
        t[i] = np.sort(t[i])
        for j in range(0,n):
            count = 1
            for k in range(0,n-1):
                if (t[i,k] == 0 and count == 1):
                    t[i,k] = t[i,k+1]
                    t[i,k+1] = 0
                if (t[i,k] == 0 and count < 1):
                    count += 1
    for i in range(0,n):
        C[i] = calcC(t)
    return t,C
    
def calcT(a):
    t = np.roots(a)
    return t
    
def calcC(t):
    m = len(t)
    A = np.zeros([m,m])
    b = np.zeros(m)
    for i in range(0,m)[::2]:
        b[i] = 2/(i+1)
    for i in range(0,m):
        for j in range(0,m):
            A[i,j] = t[m-1,j]**i
    return decompLU(A,b)