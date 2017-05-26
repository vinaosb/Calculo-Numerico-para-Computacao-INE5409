import numpy as np

def Restos(n,a,xI):
    b = np.zeros(n)
    r = np.zeros(len(xI))
    
    for i in range(0,len(xI)):
        b[0] = a[0]
        for j in range(1,n):
            b[j] = a[j] + xI[i]*b[j-1]
        r[i] = b[n-1]
    return r