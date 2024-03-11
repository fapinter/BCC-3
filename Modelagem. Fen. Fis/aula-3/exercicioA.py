import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# 𝑓 𝑥 = 𝑥2, 𝑓 𝑥 = 2𝑥 no intervalo −2 ≤ 𝑥 < 2, 𝑓 𝑥 = cos(𝑥) e 𝑓 𝑥 = sin(𝑥)

x = sp.Symbol('x')


x1_grafico = []
x2_grafico = []
y1_grafico = []
y2_grafico = []

seno_grafico = []
cosseno_grafico = []
ySeno = []
yCosseno = []
contador = 0

for x in range(-2, 3):

    x1_grafico.append(x)
    y1_grafico.append(x**2)

    x2_grafico.append(x)
    y2_grafico.append(2 * x)

    
    seno_grafico.append(x)
    ySeno.append(np.sin(seno_grafico[contador]))
    cosseno_grafico.append(x)
    yCosseno.append(np.cos(cosseno_grafico[contador]))
    contador += 1 



x_grafico = np.arange(-3,3,1)
print(ySeno)
print(yCosseno)


plt.plot(x1_grafico,y1_grafico, 'r')
plt.show()


plt.plot(x2_grafico,y2_grafico,'b')
plt.show()

plt.plot(seno_grafico,ySeno, 'k')
plt.plot(cosseno_grafico,yCosseno, 'y')
plt.show()



