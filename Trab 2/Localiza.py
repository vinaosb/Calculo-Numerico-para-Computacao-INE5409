import numpy as np

def Localiza(n,a):
    raioMax = np.zeros(3)
    raioMin = np.zeros(3)
    """cota do modulo maximo"""
    aux1 = np.zeros(n)
    aux2 = np.zeros(n)
    aux1 = np.divide(np.abs(a[1:n]),np.abs(a[0]))
    aux2 = np.divide(np.abs(a[0:n-1]),np.abs(a[n-1]))
    raioMax[0] = np.add(1 , max(aux1))
    raioMin[0] = np.divide(1,(np.add(1 , max(aux2))))
    
    
    """cota de gauchy"""
    """max"""
    rI = np.divide(np.abs(a[n-1]),np.abs(a[0]))**(1/(n-1))

    for k in range(0,30):
        soma = np.abs(np.divide(a[n-1],a[0]))
        for i in range(1,n-1):
            soma += np.multiply(np.abs(np.divide(a[i],a[0])),(rI))**(n-i)
        raioMax[1] = soma ** (1/n-1)
        rI = raioMax[1]
    
    """min"""
    rI = (abs(np.divide(a[0],a[n-1]))**(1/(n-1)))
    for k in range(0,30):
        soma = np.abs(np.divide(a[0],a[n-1]))
        for i in range(1,n-1):
            soma += np.multiply(np.abs(np.divide(a[i],a[n-1])),(rI))**(i)
        rI = soma**(1/(n-1))
    raioMin[1] = np.divide(1,rI)
    
    
    
    """cota kojima"""
    """max"""
    q = np.zeros(n)
    ordenado = np.zeros(n)
    for i in range(1,n):
        q[i] = np.abs(np.divide(a[i],a[0]))**(1/i)
    ordenado = np.sort(q)
    max1 = ordenado[n-1]
    max2 = ordenado[n-2]
    raioMax[2] = max1+max2
    
    """min"""
    for i in range(1,n):
        q[i] = np.abs(np.divide(a[n-i],a[n-1]))**(1/i)
    ordenado = np.sort(q)
    max1 = ordenado[n-1]
    max2 = ordenado[n-2]
    raioMin[2] = max1+max2
    
    rmax = min(raioMax)
    rmin = max(raioMin)
    
    raioMedio = ((rmin + rmax)/2)
    a = raioMedio*np.cos(np.pi/4)
    b = -a
    xI = complex(a,b)
    return xI