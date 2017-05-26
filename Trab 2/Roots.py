import numpy as np

def Roots(a):
    tol = 1e-10
    n = len(a)
    nI = n
    aI = a
    indiceRaiz = 0
    x = np.zeros(n,dtype=np.complex_)
    xI = np.zeros(n,dtype=np.complex_)
    lantRaiz = np.zeros(n)
    lantRef = np.zeros(n)
    M = np.zeros(n)
    k = 0
    itNR = np.zeros(2)
    while((n > 1)):
        """Funcao para localizar as raizes iniciais"""
        xI[indiceRaiz] = Localiza(n,a)
        
        """Newton Raphson para achar raiz aproximada"""
        [x[indiceRaiz], M[indiceRaiz], k, lantRaiz] = NRPoli(n,a,xI[indiceRaiz],tol)
        itNR[0] += k
        
        """Newton Raphson para refinar valor da raiz aproximada"""
        [x[indiceRaiz], M[indiceRaiz], k, lantRef] = NRPoli(nI,aI,x[indiceRaiz],tol)
        itNR[1] += k
        
        """Briot Ruffini para reduzir o grau do polinomio"""
        [n,a] = DivPol(n,a,x[indiceRaiz],M[indiceRaiz])
        
        indiceRaiz += 1
    c = np.zeros(19)
    for i in range(0,19):
        c[i] = 10**(-(i+1))
    print("\n\nValor otimizado se tiver apenas 1 Newton Raphson:" , 10**-np.max(lantRaiz))
    print("Valor otimizado caso tenha 2 Newton Raphson (com refinamento):", 10**-np.max([np.max(lantRaiz),np.max(lantRef)]))
    print("\nValores testados:",c)
    print("\n\n\nIteracoes Newton Raphson com polinomio reduzido:",itNR[0])
    print("\nIteracoes Newton Raphson com polinomio original:",itNR[1])
    print("\nIteracoes totais efetuadas:",itNR[0] + itNR[1],"\n\n\n")
    return [x[0:len(x)-1],M[0:len(M)-1],xI[0:len(xI)-1]]
