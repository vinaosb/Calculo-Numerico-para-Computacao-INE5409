import numpy as np


def coef(n):
    y = 1/fac(n)
    return y

def tcheby(x,n):
    T = np.zeros([n+1,len(x)])
    T[0] = 1
    T[1] = x
    for i in range(2,n+1):
        T[i] = ((2*x*T[i-1]) - T[i-2])
    C = T[1]
    C = C - (((T[3] + 3*T[1])/4)*coef(3))
    if(n >= 5):
        C = C + (((T[5] + 5*T[3] + 10*T[1])/16)*coef(5))
        if (n >= 7):
            C = C + (((7*T[5] + 21*T[3] + 35*T[1])/64)*coef(7))
        else:
            C = C - coef(5)*T[5]/16
    return C

