import numpy as np


def fx3(i,x):
    
    Tt = [ 0.00,     0.39,   0.78,   1.18 ] 
    Vv = [ 0.99,     0.92,   0.71,   0.38 ] 
    m = len(Tt)
    


    if(i == 0):
        y = 0
        for k in range(0,m):
            y += ((x[0]*Tt[k]+x[1]*np.cos(Tt[k]))-Vv[k])*Tt[k]
        return y
    if(i == 1):
        y = 0
        for k in range(0,m):
            y += ((x[0]*Tt[k]+x[1]*np.cos(Tt[k]))-Vv[k])*np.cos(Tt[k])
        return y