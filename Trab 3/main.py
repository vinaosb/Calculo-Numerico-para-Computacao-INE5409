import numpy as np
import matplotlib.pylab as plt


print("Capitulo 5")
print("2a)\n")
xs = [0,1,2,3]
ys = [-3,-2,4,0]
[a,b,c,d] = spline(xs,ys)
print("a =",a[1],"\nb =",b[1],"\nc =",c[1],"\nd =",d[1])
xv = np.linspace(0,3,301)
yv = np.zeros(len(xv))
j = 0
i = 0
while(xv[i] < 3):
    if(xv[i] == 1 or xv[i] == 2):
        j += 1
    yv[i] = a[j]*(xv[i] - xs[j])**3 + b[j]*(xv[i] - xs[j])**2 + c[j]*(xv[i] - xs[j]) + d[j]
    i += 1
xk = 1.3
i = 0
while(xk > xv[i]):
    i += 1
print("\n2c e d)","\nO valor desejado e:",yv[i])
plt.figure(5)
plt.title("Spline")
plt.plot(xv,yv,'g',xs,ys,"ro")
print("\n2e) Plotado")

print("\n3) Feito")
xb = [0,2,8,10]
yb = [0,1,0.2,0]
q = [45,0,-15,-8,-8,-5]

[xn,yn] = bernier(xb,yb,q)
plt.figure(6)
plt.title("Bezier")
plt.plot(xn,yn,'r',xb,yb,"bo")

print("\n\n4a)\n")
print("Com n = 3, temos que F'''' = sen(x)\n com isso usa-se diretamente na formula do erro com o valor maximo =\n abs((sen(pi/2)*(pi/6)^(3+1))/4*(3+1)) = 4.6e-3 \nque esta dentro da ordem -2\n")

print("4b)\n")
npontos = 3
x4 = np.linspace(0,np.pi/2,npontos)
y4 = np.zeros(npontos)
for k in range(0,npontos):
    y4[k] = np.sin(x4[k])

k = np.linspace(0,np.pi/2,npontos*20)
Y = np.zeros(len(k))
for m in range(0,len(k)):
    Y[m] = GregoryNewton(k[m],x4,y4,npontos)
Erro4 = np.max(np.abs(np.sin(k) - Y))
print("Valor de x e y:\n",x4,"\n",y4)

print("4c)\n")
print("Erro de truncamento Greg Newton:\n",Erro4,"\n")

print("4d)\nPlotado")
npontos = 5
x4 = np.linspace(0,np.pi/2,npontos)
y4 = np.zeros(npontos)
for k in range(0,npontos):
    y4[k] = np.sin(x4[k])

k = np.linspace(0,np.pi/2,100)
Y = np.zeros(len(k))
for m in range(0,len(k)):
    Y[m] = GregoryNewton(k[m],x4,y4,npontos)

Erro4 = np.max(np.abs(np.sin(k) - Y))
plt.figure(1)
plt.title("Questao 4")
plt.plot(k,Y,'r',k,np.sin(k),'b')


print("\n\n5a)")
print("Usaria interpolacao pois daria uma melhor precisao ja que podemos gerar os pontos exatos.")

print("\n5b) nao esta feito, pois nao tive tempo de converter para python\n")

print("\n5c)")
x5 = np.linspace(0,1,3)
y5 = np.zeros(len(x5))
for k in range(0,len(x5)):
    y5[k] = np.exp(x5[k])
    
k = np.linspace(0,1,40)
Y = np.zeros(len(k))

for m in range(0,len(k)):
    Y[m] = P(k[m],x5,y5)
Erro5 = np.max(np.abs(np.exp(0.378) - P(0.378,x5,y5)))
print("Resposta: ",P(0.378,x5,y5),"\nErro:",Erro5)


print("\n5d)")
npontos = 3
x5 = np.linspace(0,1,npontos)
y5 = np.zeros(len(x5))
for k in range(0,len(x5)):
    y5[k] = np.exp(x5[k])

k = np.linspace(0,np.pi,npontos*2)
Y = np.zeros(len(k))
for m in range(0,len(k)):
    Y[m] = GregoryNewton(k[m],x5,y5,npontos)
Erro5 = np.max(np.abs(np.exp(0.378) - GregoryNewton(0.378,x5,y5,npontos)))
print("Resposta:",GregoryNewton(0.378,x5,y5,npontos),"\nErro:",Erro5)

print("\n\n6a):")
n = 5
x6 = np.linspace(0,np.pi/2,n)
y6 = np.zeros(len(x6))
for k in range(0,len(x6)):
    y6[k] = np.cos(x6[k])
    
k = np.linspace(0,np.pi/2,100)
Y = np.zeros(len(k))

for m in range(0,len(k)):
    Y[m] = P(k[m],x6,y6)
Erro6 = np.abs(np.cos(k) - Y)
Erro6max = np.max(Erro6)
print("\nErro:",Erro6max)
plt.figure(2)
plt.title("Questao 6a")
plt.plot(k,Erro6,'r')

print("\n6b)")
tol = np.sqrt(10)*1e-6
n = 3
k = np.linspace(0,np.pi/2,100)
Y = np.zeros(len(k))
while(Erro6max > tol and n <20):
    n=n+1
    x6 = np.linspace(0,np.pi/2,n)
    y6 = np.zeros(len(x6))
    for l in range(0,len(x6)):
        y6[l] = np.cos(x6[l])
    
    for m in range(0,len(k)):
        Y[m] = P(k[m],x6,y6)
    Erro6 = np.abs(np.cos(k) - Y)
    Erro6max = np.max(Erro6)
print("Numero de pontos (grau +1):",n,"\nErro:",Erro6max)
plt.figure(3)
plt.title("Questao 6b")
plt.plot(k,Erro6,'r')


print("\n\nCapitulo 6\n")
print("1a)")
tol = np.sqrt(10)*1e-2
n = 2
k = np.linspace(-1,1,100)
Y = np.zeros(len(k))
Erro1max = 1
while(Erro1max > tol and n <20):
    n=n+1
    x1 = np.linspace(-1,1,n)
    y1 = np.zeros(len(x1))
    for l in range(0,len(x1)):
        y1[l] = np.sin(x1[l])
    
    for m in range(0,len(k)):
        Y[m] = P(k[m],x1,y1)
    Erro1 = np.abs(np.sin(k) - Y)
    Erro1max = np.max(Erro1)
print("Numero de pontos (grau +1):",n,"\nErro:",Erro1max)

print("\n\n1b)\n")
xe = np.linspace(-1,1,11)
ye = np.sin(xe)

erromacmax = 1.
n = 0
while(erromacmax > tol):
    n += 1
    yM = maclaurin(xe,n)
    erromac = np.abs(yM - ye)
    erromacmax = np.max(erromac)
print("O grau n otimizado seria: ",n,"\nOs coeficientes seriam 1 - 1/6 + 1/24","\nE o erro maximo e:",erromacmax)
    
    
print("\n\n1c)\n")
yC = tcheby(xe,5)
errotche = np.abs(yC - ye)
errotchemax = np.max(errotche)
print("Partindo de um polinomio com n = 5, e ignorando o T5 (para reduzir para n=3) \ntemos os coeficientes:",[0,383/384,0,-5/32,0,0],"\nO erro maximo calculado foi:",errotchemax)

print("\n1d)\n")
yC = tcheby(xe,7)
errotchemax = np.max(np.abs(yC - ye))
print("Partindo de um polinomio com n = 7, e ignorando o T7 (para reduzir para n=5) \ntemos os coeficientes:\n",[0,11521/11520,0,-959/5760,0,23/2880,0,0],"\nO erro maximo calculado foi:",errotchemax)

print("\n1e)\n")
yp = pade(xe,5)
erropade = np.max(np.abs(yp - ye))

print("\n1f) Plotado")
plt.figure(4)
plt.title("Capitulo 6f")
plt.plot(xe,yM,'r',xe,yC,'b',xe,yp,'g')
plt.show