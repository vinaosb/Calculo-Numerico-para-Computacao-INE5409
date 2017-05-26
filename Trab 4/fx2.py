import numpy as np


def fx2(i,x):
    
    T=[ 0.2,    0.4,    0.6,    0.8,   0.9,   1.0  ]
    V=[ 0.04,   0.14,   0.30,   0.45,  0.61,  0.69 ]
    m = len(T)
    


    if(i == 0):
        y = 0
        for k in range(0,m):
            y += (np.log(x[0]+x[1]*T[k]**2)-V[k])*1/(x[0]+x[1]*T[k]**2)
        return y
    if(i == 1):
        y = 0
        for k in range(0,m):
            y += (np.log(x[0]+x[1]*T[k]**2)-V[k])*(T[k]**2)/(x[0] + x[1]*(T[k]**2))
        return y