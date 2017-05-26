import numpy as np

def pade(x,n):
    c = np.zeros(n)
    for i in range(0,n):
        c[i] = coef(i)
    c[0] = 0
    c[2] = 0
    c[3] = -c[3]
    c[4] = 0
    print(c)
    A1 = ([c[2],c[1]],[c[3],c[2]])
    A2 = ([-c[3],-c[4]])
    b = gauss(A1,A2)

    
    a = np.zeros(n)
    a = (c[0],b[0]*c[0] + c[1], b[1]*c[0] + b[0]*c[1] + c[2], c[2]*b[0] + c[1]*b[1] + c[3], c[4] + c[3]*b[0] + c[2]*b[1])
    
    yp = ((a[0] + a[1]*x + a[2]*(x**2) + a[3]*(x**3))/(1 + b[0]*x + b[1]*x**2))
    return yp