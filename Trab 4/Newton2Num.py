import numpy as np

def Newton2Num(xi):
    tol = 1e-15
    difAnt = 1e-10
    difDif = 1
    dif = 1
    n = len(xi)
    k = 0
    dx = np.multiply(np.ones(n),1e-6)
    A = np.zeros([n,n])
    b = np.zeros(n)
    temp = np.zeros(n)
    
    while(dif > tol and difDif > tol and k < 150):
        k += 1
        for i in range(0,n):
            for j in range(0,n):
                for k in range(0,n):
                    temp[k] = xi[k] + (j==k)*dx[k]
                A[i,j] = (fx2(i,temp) - fx2(i,xi))/dx[j]
            b[i] = -fx2(i,xi)
            
        dx = decompLU(A,b)
        x = xi+dx
        xi = x
        dif = np.max(np.abs(dx))
        difDif = np.abs(dif-difAnt)
        difAnt = dif
    return x