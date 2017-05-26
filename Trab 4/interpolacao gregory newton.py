import numpy as np


def DiferencaDividida(x,y,m):
    k = 0
    DDy = np.zeros([m,m])
    for i in range(0,m-1):
        DDy[k,i] = (y[i+1]-y[i])/(x[i+1] - x[i])
    for k in range(1,m-1):
        for i in range(1,m-k):
            DDy[k,i-1] = (DDy[k-1,i]-DDy[k-1,i-1])/(x[i+k] - x[i-1])
    return DDy

def GregoryNewton(x,a,b,n):
    DDy = DiferencaDividida(a,b,n)
    yPn = np.zeros(len(x))
    for i in range(0,len(x)):
        soma = b[0]
        for k in range(0,len(a)):
            produto = 1.
            for j in range(0,k+1):
                produto = produto*(x[i] - a[j])
            soma += DDy[k,0]*produto
        yPn[i] = soma
    return yPn,DDy[0:len(DDy)-1,0]

