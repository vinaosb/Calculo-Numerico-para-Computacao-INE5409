import numpy as np


def Trapezios(n,a,b):
    x = np.linspace(a,b,n+1)
    y = fx1(x)
    soma = 0
    for i in range(1,n):
        soma += y[i]
    
    return 0.5*((b-a)/n)*(y[0] + (2*soma) + y[n])