import numpy as np

a = [np.complex(1,0), - np.complex(5,1), np.complex(9.99,5), - np.complex(9.97,9.99), np.complex(4.97,9.97), - np.complex(0.99,4.97), np.complex(0,0.99)]
O = [np.complex(1.11022302462516e-016, - 9.99999999999998e-001),np.complex(-1.10000000001157e+000, - 1.66881099646068e-011),np.complex(-9.00000000006002e-001, - 1.03123087860931e-011),np.complex(-1.00005167555860e+000, + 4.50036411031659e-005),np.complex(-9.99935195062783e-001, + 2.22505634491045e-005),np.complex(-1.00001312936105e+000, - 6.72541775503178e-005)]
W = [np.complex(0.9,0), np.complex(0.999959,0), np.complex(1.1,0), np.complex(0,1), np.complex(1.00002,-0.0000351069), np.complex(1.00002,0.0000351069)]
E = [0.9,1,1,1,1.1,np.complex(0,1)]
P = np.roots(a)

[x,M,xI] = Roots(a)

print("Valores das Raizes")
for i in range(0,len(x)):
    print("\nRaiz numero:", i+1, "\nValor:", x[i], "\nMultiplicidade:" , M[i],"\nChute inicial:", xI[i])
print("\n\nValor das raizes pelo Octave:", O)
print("\n\nValor das raizes pelo Wolfram:", W)
print("\n\nValor das raizes pelo Phyton:", P)
print("\n\nValor exato:", E)

"""Achar o erro total do metodo:"""
X = np.sort(np.abs(x)*M)
o = np.sort(np.abs(O))
w = np.sort(np.abs(W))
e = np.sort(np.abs(E))
p = np.sort(np.abs(P))
for i in range(0,len(x)):
    X[i] = X[i]-e[i]
    o[i] = o[i]-e[i]
    w[i] = w[i]-e[i]
    p[i] = p[i]-e[i]
aux = np.zeros(4)
for i in range(0,len(x)):
    aux[0] += X[i]
    aux[1] += o[i]
    aux[2] += w[i]
    aux[3] += p[i]
aux = np.abs(aux)
print("\nDiferencas absolutas dos valores descobertos com o valor exato (erro total):","\nDiferenca pelo codigo:",aux[0],"\nDiferenca pelo Octave:", aux[1], "\nDiferenca pelo Wolfram",aux[2], "\nDiferenca pelo Roots do Phyton",aux[3])
print("\nCom esses valores tem-se que o melhor valor e o do Roots do Phyton, seguido pelo do Octave, seguido do valor do Wolfram, e o pior sendo o do codigo feito.")