import numpy as np



def DivPol(n,a,x,M):
    b = np.zeros(n,dtype=np.complex_)
    for j in range(0,np.int(M)):
        b[0] = a[0]
        for i in range (1,n):
            b[i] = np.add(a[i], np.multiply(x,b[i-1]))
        n = n -1
        a = b
    aux = a[0:n]
    a = aux
    return [n,a]