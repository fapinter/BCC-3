import sympy as sp
import numpy as np


x = sp.Symbol('x')

funcao = x**2

limite0 = sp.limit(funcao,1,x)
print(limite0)

limite1 = sp.limit(funcao,-1.2,x)
print(limite1)