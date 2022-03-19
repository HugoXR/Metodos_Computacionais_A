# Resolucao de sistemas nao lineares
import numpy as np
import matplotlib.pyplot as plt
import time


def F(X):
    return np.array([np.sin(X[0]**2 + X[1]**2), 2*X[0] - X[1] - 1/(X[0] + X[1])])


nplot = 200
lim_plot = np.array([[0, 3], [0, 3]])
xplot = np.repeat(np.linspace(lim_plot[0, 0], lim_plot[0, 1], nplot), nplot).reshape([nplot, nplot]).T
yplot = np.repeat(np.linspace(lim_plot[1, 0], lim_plot[1, 1], nplot), nplot).reshape([nplot, nplot])
zplot = F([xplot, yplot])


fig = plt.figure()
for i in [0, 1]:
    ax = fig.add_subplot(1, 3, i+1, projection='3d')
    ax.plot_surface(xplot, yplot, zplot[i]*(zplot[i] > 0), cmap=plt.get_cmap('inferno'))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.gca().set_zlabel('z')


def J(X):
    cos_X = np.cos(X[0]**2 + X[1]**2)
    inv_x = 1/(X[0] + X[1])**2
    jacobiano = np.array([[2*X[0]*cos_X, 2*X[1]*cos_X], [2 + inv_x, -1 + inv_x]])
    return jacobiano


def Newton_Raphson(F, J, X0, erroMaximo=1E-10):
    erro = 1E10
    passos = np.array([X0])
    n = 0
    while(erro > erroMaximo) and (n<100):
        n += 1
        delta_x = np.linalg.solve(J(X0), -F(X0))
        X0 += delta_x
        passos = np.vstack([passos, X0])
        erro = np.abs(delta_x).max()
    return X0, passos


fig.add_subplot(1, 3, 3)
X0 = np.array([0.5, 1])
X1, passos = Newton_Raphson(F, J, X0)
plt.plot(passos[:, 0], passos[:, 1], '-o')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
plt.close('all')
