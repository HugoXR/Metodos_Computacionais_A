import numpy as np
import matplotlib.pyplot as plt

# Lendo valores de x e y e atribuindo a uma array
data = np.loadtxt('xy.dat', dtype=float)

x = data[:, 0] # Valores de x da array
y = data[:, 1] # Valores de y da array

y_max = y.max() # Maior valor de y
y_min = y.min() # Menor valor de y

y_mean = (y.sum()/len(y)) # Media de y

print(f" Max of y is {y_max:.2f}\n Min of y is {y_min:.2f}\n Mean of y is {y_mean:.2f}")

#Plotando os valores de x e y
plt.plot(x, y, "-b")
plt.show()

