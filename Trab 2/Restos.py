import numpy as np

def Restos(n,a,xI):
    b = np.zeros(n,dtype=np.complex_)
    r = np.zeros(n,dtype=np.complex_)
    nI = n
    
    for i in range(0,nI-1):
        b[0] = a[0]
        for j in range(1,n):
            b[j] = np.add(a[j], np.multiply(xI,b[j-1]))
        r[i] = b[n-1]
        n = n-1
        a = b
    r[nI-1] = b[0];
    return r