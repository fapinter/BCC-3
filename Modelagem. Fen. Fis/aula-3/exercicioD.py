import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as pa


numeroVertices = int(input("Quantos vertices o poligono via ter: "))


centro_grafico = [0.5,0.5]

fig, ax = plt.subplots(figsize = (12, 8))
plt.gca().add_patch(pa.RegularPolygon(centro_grafico,numeroVertices,radius=0.2,orientation = 0))
plt.title("Poligono Escolhido")
plt.show()