import numpy as np


def IntGauss(a,b,m):
    t,C = PolLegendre(m)
    soma = 0
    x = np.zeros(m)
    y = np.zeros(m)
    for  k in range(0,m):
        x[k] = (b-a)*t[m-1][k]/2 + (b+a)/2
        y[k] = fx1(x[k])
        soma += C[m-1][k]*y[k]
    return 0.5*(b-a)*soma,x,y