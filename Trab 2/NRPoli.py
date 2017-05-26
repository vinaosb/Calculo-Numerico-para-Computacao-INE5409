import numpy as np

def NRPoli(n,a,xI,tol):
    dif2 = 1
    dif = 1
    k = 0   
    M = 6
    lant = n
    
    while((dif > tol) and (k < 1000)):
        k += 1
        r = Restos(n,a,xI)
        [M,l] = Multiplicidade(r)

        dx = - r[M-1]/(M*r[M])
        x = xI + dx
        xI = x
        
        dif = np.abs(dx)+abs(r[0])
        dif = np.abs(dif2 - dif)
        dif2 = np.abs(dx)+abs(r[0])
        if(l > lant):
            lant = l
    return [x,M,k,lant]
    