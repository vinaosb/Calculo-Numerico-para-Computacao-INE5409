import numpy as np
from scipy.integrate import quad
import matplotlib.pylab as plt


T=[ 0.2,    0.4,    0.6,    0.8,   0.9,   1.0  ]
V=[ 0.04,   0.14,   0.30,   0.45,  0.61,  0.69 ]

M = len(T)

Xi = [0.01,0.01]
S = Newton2Num(Xi)
A = S[0]
B = S[1]

D = np.abs(np.log(A + np.multiply(B,np.power(T,2))) - V)

Tp = np.linspace(T[0],T[len(T)-1])
Vp = np.log(A + np.multiply(B,(Tp**2)))
Yip,DDy = GregoryNewton(Tp,T,V,M)

print("Capitulo 7")
print("\nQuestao 1")
print("\nQuestao 1a)\nCoeficientes:\na = ",A,"\nb = ",B)
print("\nQuestao 1b)\nModulo do Desvio Local =\n",D)
print("\nQuestao 1c)\nPlotado")

plt.figure(1)
plt.title("Questao 1")
plt.plot(T,V,"go",label="Pontos")
plt.plot(Tp,Vp,'k',label="Aproximacao")
plt.plot(Tp,Yip,"--r",label="Interpolacao")
plt.legend(loc="upper left")



print("\n\n\nQuestao 2)")
print("\nQuestao 2a)")
print("Empregaria a funcao interpoladora quando tivesse valores exatos ou a funcao exata,\ne empregaria ajuste quando tivessem erros nas medicoes")
print("\nQuestao 2b)")
print("Passar por todos os pontos dados")
print("\nQuestao 2c)")
print("Passar o mais proximo possivel dos pontos dados de modo a ter o menor desvio possivel")
print("\nQuestao 2d)")
print("Quando usa-se um polinomio Pn com n+1 pontos estamos obtendo um polinomio sem desvio, ou seja passa exatamente em cima dos pontos tabelados\ncom isso temos que ele equivale ao proprio polinomio interpolador pela sua definicao")


t=[ 13.9,       37.0,   67.8,   79.0,   85.5,   93.1,   99.2] 
v=[ 1.04,       1.18,   1.29,   1.35,   1.28,   1.21,   1.06] 
m = len(t)
tp = np.linspace(t[0],t[len(t)-1])

s = detAjustePn(t,v,1)
yia1 = PnH(1,s,tp)

ss = detAjustePn(t,v,2)
yia2 = PnH(2,ss,tp)


yip,ddy = GregoryNewton(tp,t,v,m)

print("\n\n\nQuestao 3)")
print("\nQuestao 3a)")
print("Coeficientes a e b do primeiro grau:",s,"\nCoeficientes a e b do segundo grau:",ss)
print("\nQuestao 3b)")
print("Diferenca dividida:\n",ddy)
print("\nQuestao 3c)")
print("Plotado")
print("\nQuestao 3d)")
print("Usarei a de segundo grau que aparenta melhor no grafico, \ndevido a interpolacao ser muito sinuosa e a linear nao captar a curvatura dos pontos")


plt.figure(3)
plt.title("Questao 3")
plt.plot(t,v,"go",label="Pontos")
plt.plot(tp,yia1,'-.k',label="Aproximacao 1o Grau")
plt.plot(tp,yia2,"b",label="Aproximacao 2o Grau")
plt.plot(tp,yip,"--r",label="Interpolacao")
plt.legend(loc="upper left")


Tt = [ 0.00,     0.39,   0.78,   1.18 ] 
Vv = [ 0.99,     0.92,   0.71,   0.38 ] 
Mm = len(Tt)

Xii = [0.01,0.01]
print("\n\n\nQuestao 4)")
print("\nQuestao 4a)")
Ss = Newton2Num2(Xii)
print("Coeficientes a e b:",Ss)
Aa = Ss[0]
Bb = Ss[1]

Dd = np.abs(np.multiply(Aa,Tt) + np.multiply(Bb,np.cos(Tt)) - Vv)
Tt2 = np.subtract(Tt,0.075)

print("\nQuestao 4b)")
print(Dd)

plt.figure(4)
plt.title("Questao 4")
plt.bar(Tt2,Dd,width=0.15)
plt.show



a = 0
b = 1
Exato = quad(fx1,a,b)[0]
tol = np.sqrt(10)*1e-6

#Metodo dos Trapezios
niT = 0
ErroExatoT = 1
while(ErroExatoT > tol and niT < 1000):
    niT += 1
    Tn = Trapezios(niT,a,b)
    #EstimadoT = Trapezios(niT*2,a,b)
    #ErroT = np.abs(Tn - EstimadoT)
    ErroExatoT = np.abs(Tn - Exato)


#Metodo de Simpson
niS = 3
ErroExatoS = 1
while(ErroExatoS > tol):
    niS += 1
    Sn = Simpson(niS,a,b)
    EstimadoS = Simpson(niS*2,a,b)
    ErroS = np.abs(Sn - EstimadoS)
    ErroExatoS = np.abs(Sn - Exato)

#Metodo de Gauss
niG = 1
ErroExatoG = 1
while(ErroExatoG > tol):
    niG += 1
    Gn,x,y = IntGauss(a,b,niG)
    ErroExatoG = np.abs(Gn - Exato)

#Polinomio usando x,y do metodo de Gauss
xG = np.linspace(a,b,101)
coefPol,yG = inter(xG,x,y,niG)
intPol = (coefPol[0]/4)+(coefPol[1]/3)+(coefPol[2]/2)+(coefPol[3])
#Polinomio usando x e y da funcao
xP = np.linspace(a,b,100)
yP = fx1(xP)
ErroPol = np.abs(intPol-Gn)

print("\n\n\nCapitulo 8:")
print("Valor exato para comparacao:",Exato)
print("\nQuestao 6.a)")
print("O n minimo para essa tolerancia e para o valor exato (nao estimado e sim exato) eh:",niT,"\nO erro exato seria:",ErroExatoT)
print("\nQuestao 6.b)")
print("O n minimo para essa tolerancia e para o valor exato (nao estimado e sim exato) eh:",niS,"\nO erro exato seria:",ErroExatoS)
print("\nQuestao 6.c)")
print("O n minimo para essa tolerancia e para o valor exato (nao estimado e sim exato) eh:",niG,"\nO erro exato seria:",ErroExatoG)
print("\nQuestao 6.d)")
print("Os coeficientes do interpolador seriam:\n",coefPol[0],"*x^3 +",coefPol[1],"*x^2 +",coefPol[2],"*x^1 +",coefPol[3])
print("\nQuestao 6.e)")
print("O valor da integral pelo interpolador eh:", intPol, "\nErro:",ErroPol)
print("\nQuestao 6.f)")
print("Plotado")

plt.figure(6)
plt.title("Exercicio 6f)")
plt.plot(xP,yP,'r',label="Funcao")
plt.plot(x,y,"go",label="Pontos")
plt.plot(xG,yG,'b',label="Polinomio")
plt.legend(loc="upper left")
plt.show