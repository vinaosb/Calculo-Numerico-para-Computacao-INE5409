import numpy as np



def gauss(A,b):

    N = len(A)

    AM = np.zeros([N,N+1])
    AM[:,0:N] = A
    AM[:,N] = b
    count = 0                   ##numero de operacoes

    for j in range(0,N-1):    ##confere se a matriz tem elemento na diag principal igual a 0 e muda a linha caso ocorra
        for l in range(j + 1,N):
            if (AM[j,j] == 0 and AM[l,j] != 0):
                temp = np.zeros([N+1])
                temp = AM[j,:].copy()
                AM[j,:] = AM[l,:].copy()
                AM[l,:] = temp.copy()
            else:              ##confere se a matriz e impossivel ou indeterminada
                if(AM[j,j] == 0 and AM[l,j] == 0 and l == N-1 and AM[N-1,N] == 0):
                    print("Sistema Indeterminado\n\n")
                    return np.zeros(N)
                else:
                    if(AM[j,j] == 0 and AM[l,j] == 0 and l == N-1):
                        print("Sistema Impossivel\n\n")
                        return np.zeros(N)


        else:                           ##eliminacao gaussiana
            for i in range (j+1,N):
                if AM[i,j] != 0:
                    k = AM[i,j]/AM[j,j]
                    AM[i,:] = AM[i,:] - (AM[j,:]*k)
                    count = count + 4



    x = np.zeros(N)


    for i in range(0,N)[::-1]:  ##resolucao do sistema
        soma = 0
        for j in range(i+1,N):
            soma = soma + AM[i,j] * x[j]
            count = count +2
        x[i] = (AM[i, N] - soma) / AM[i,i]
        count = count + 2
    return x


