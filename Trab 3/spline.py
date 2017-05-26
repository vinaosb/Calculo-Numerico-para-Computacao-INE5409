import numpy as np


def Splineb(m,x,y,h):
    """A = np.zeros([m+1,m+1])
    A[0,0] = 3*h[0] + 2*h[1]
    A[0,1] = h[0]
    b = np.zeros(m+1)
    b[0] = 6*((y[2]-y[1])/(h[1]) - (y[1]-y[0])/h[0])
    for i in range(1,m):
        A[i,i-1] = h[i-1]
        A[i,i] = 2*(h[i-1]+h[i])
        A[i,i+1] = h[i]
        b[i] = 6*((y[i+1]-y[i])/h[i] - (y[i]-y[i-1])/h[i-1])
    A[m,m-1] = h[m-2]
    A[m,m] = (2*h[m-2]+3*h[m-1])
    b[m] = 6*((y[m]-y[m-1])/h[m-1] - (y[m-1] - y[m-2]/h[m-2]))
    print(A,b)
    S = gauss(A,b)
    print(S)"""
    t = np.zeros(1+m)
    r = np.zeros(1+m)
    d = np.zeros(1+m)
    b = np.zeros(1+m)
    
    t[0] = 0
    r[0] = 3*h[0] + 2*h[1]
    d[0] = h[0]
    b[0] = 6*((y[2]-y[1])/(h[1]) - (y[1]-y[0])/h[0])
    for i in range(1,m):
        t[i] = h[i-1]
        r[i] = 2*(h[i-1]+h[i])
        d[i] = h[i]
        b[i] = 6*((y[i+1]-y[i])/h[i] - (y[i]-y[i-1])/h[i-1])

    t[m] = h[m-2]
    r[m] = (2*h[m-2]+3*h[m-1])
    d[m] = 0
    b[m] = 6*((y[m]-y[m-1])/h[m-1] - (y[m-1] - y[m-2]/h[m-2]))
    
    for i in range(1,m):
        aux = t[i]/r[i-1]
        t[i] = 0
        r[i] = r[i] - aux*d[i-1]
        b[i] = b[i] - aux*b[i-1]
    S = np.zeros(m+1)
    S[m] = b[m]/r[m]
    for i in range(0,m)[::-1]:
        S[i] = (b[i]-d[i]*S[i+1])/r[i]
    S[0] = 0
    S[m] = 0
    
    f = np.zeros(m)
    g = np.zeros(m)
    l = np.zeros(m)
    k = np.zeros(m)
    
    for i in range(0,m):
        f[i] = (S[i+1]-S[i])/(6*h[i])
        g[i] = S[i]/2
        l[i] = (y[i+1]-y[i])/h[i] - (S[i+1] + 2*S[i])*h[i]/6
        k[i] = y[i]
    return [f,g,l,k]


def spline(x,y):
    n = len(x)
    ns = n-1
    h = np.zeros(ns)
    for i in range(0,ns):
        h[i] = x[i+1]-x[i]
    [a,b,c,d] = Splineb(ns,x,y,h)
    return [a,b,c,d]