import numpy as np




def PnH(n,a,x):
    y = np.zeros(len(x))
    for i in range(0,len(x)):
        y[i] = a[n]
        for j in range(0,n)[::-1]:
            y[i] = x[i]*y[i] + a[j]
    return y
