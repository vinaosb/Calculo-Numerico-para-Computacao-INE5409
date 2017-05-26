"""import numpy as np

def Multiplicidade(r):
    rLimite = (10**-5)*r[len(r)-1]
    M=1
    somaRestos = abs(r[0]) +abs(r[1])
    while (somaRestos < rLimite):
        M += 1
        somaRestos += abs(r[M])
    return M"""
    
import numpy as np
 
def Multiplicidade(r):
    Mant = len(r)+1
    
    for l in range(1,6):   
        rLimite = (10**-l)*r[len(r)-1]
        M=1
        somaRestos = abs(r[0]) +abs(r[1])
        while (somaRestos < rLimite):
            M += 1
            somaRestos += abs(r[M])
        if(M < Mant):
            Mant = M
            lant = l
        else:
            if(M == 1):
                return [Mant,lant]
    return [Mant,lant]