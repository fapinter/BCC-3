import numpy
import sympy
import matplotlib.pyplot as plt

x0 = [0.1,0.2,0.3,0.4]
x1 = [1.1, 1.3, 1.5, 1.8, 2]
x2 = [2.5, 3, 4, 6]

y0 = [1 for i in x0]
y1 = [2 * x for x in x1]
y2 = [4 for i in x2]

plt.plot(x0,y0, marker="3")
plt.grid()
plt.title("X sendo menor que 1")
plt.show()
plt.plot(x1,y1,linestyle="-")
plt.title("X  entre 1 < x <=2")
plt.show()
plt.plot(x2,y2,linestyle="--")
plt.title("X < 2")
plt.show()