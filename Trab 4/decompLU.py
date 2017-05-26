import numpy as np

def identity(n):
	A = np.zeros( [n,n ] )
	for i in range(0,n):
		A[i,i] = 1.0
	return A
    
def LUfactorization(A):
    n = len(A)
    L = identity(n)
    U = identity(n)
    for j in range(n):
            for i in range(n):
                if (i <= j):
                    U[i,j] = (A[i,j] - np.dot( L[i,:] , U[:,j] ) + L[i,i] * U[i,j] )/ (L[i,i])
                else:
                    L[i,j] = (A[i,j] - np.dot( L[i,:] , U[:,j] ) + L[i,i] * U[i,j] )/ (U[j,j])
    return [L,U]
    
def somamatrizxvetor(S,x,y,k):     #k = -1 pra U e 1 pra L, S eh a matriz, x e o vetor de entrada, y eh o vetor b
    
    N = len(S)
    for i in range(0,N)[::k]:
        soma = 0
        if k == -1:
            for j in range(i+1,N):
                soma = soma + (S[i,j] * x[j])
        else:
            for j in range(0,i):
                soma = soma + (S[i,j] * x[j])
        x[i] = (y[i] - soma)/S[i,i]
    return x

def decompLU(A,b):
    L , U =  LUfactorization(A)
    
    
    N = len(L)
    c = np.zeros(N)
    x = np.zeros(N)
    """L * U * x = b
    L * [U * x] = b
    L * c = b"""
    
    c = somamatrizxvetor(L,c,b,1)
    x = somamatrizxvetor(U,x,c,-1)
    return x