import numpy as np





def detAjustePn(x,y,n):
    A = np.zeros([n+1,n+1])
    b = np.zeros(n+1)
    m = len(x)
    for i in range(0,n+1):
        for j in range(0,n+1):
            soma = 0
            for k in range(0,m):
                soma += x[k]**(i+j)
            A[i,j] = soma
            
        soma = 0
        for k in range(0,m):
            soma += y[k] * x[k]**(i)
        b[i] = soma
    return decompLU(A,b)