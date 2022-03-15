# Resolucao de sistemas nao lineares
import numpy as np
import matplotlib.pyplot as plt
import time

def F(X):
    return np.array([np.sin(X[0]**2 + X[1]**2), 2*X[0] + X[1] - 1/(X[0] + X[1])])

nplot = 100
xplot = np.repeat(np.linspace(0.01, 4, nplot), nplot).reshape([nplot, nplot]).T
yplot = np.repeat(np.linspace(0.01, 4, nplot), nplot).reshape([nplot, nplot])
zplot = F([xplot, yplot])

fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(xplot, yplot, zplot[0])
ax.plot_surface(xplot, yplot, zplot[0]*0)

ax = fig.add_subplot(122, projection='3d')
ax.plot_surface(xplot, yplot, zplot[1])
ax.plot_surface(xplot, yplot, zplot[1]*0)
plt.show()
plt.close('all')
