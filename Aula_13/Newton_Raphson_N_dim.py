# Resolucao de sistemas nao lineares
import numpy as np
import matplotlib.pyplot as plt


def F(X):
    return np.array([np.sin(X[0]**2 + X[1]**2), 2*X[0] - X[1] - 1/(X[0] + X[1])])


nplot = 50
lim_plot = np.array([[-3.00001, 3], [-3.0001, 3]])
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
    X = X0.copy()
    erro = 1E10
    passos = np.array([X])
    n = 0
    while(erro > erroMaximo) and (n < 100):
        n += 1
        delta_x = np.linalg.solve(J(X), -F(X))
        X += delta_x
        passos = np.vstack([passos, X])
        erro = np.abs(delta_x).max()
    return X, passos

g = 10
fig.add_subplot(1, 3, 3)
cm = plt.get_cmap('gist_ncar')
imagem = np.zeros([nplot, nplot, 4])
zerosF = np.array([[0, 0]])
for i in range(nplot):
    for j in range(nplot):
        X0 = np.array((xplot[i, j], yplot[i, j]))
        X1, passos = Newton_Raphson(F, J, X0)
        zerosF = np.vstack([zerosF, X1])
        gamma = X1[0]+X1[1]
        cor = cm(max(min((gamma+g)/2/g, 1), 0))
        imagem[i, j, :] = cor
        #plt.plot(passos[[0, -1], [0, 0]], passos[[0, -1], [1, 1]], '-', color=cor)
        #plt.plot(X0[0], X0[1], 's', color=cor)
        #plt.plot(X1[0], X1[1], '*', color=cor)
        #print(gamma, X0, X1, F(X1))

plt.imshow(imagem[-1:1:-1, :], extent=(lim_plot[0][0], lim_plot[0][1], lim_plot[1][0], lim_plot[1][1]))
plt.plot(zerosF[:, 0], zerosF[:, 1], 'ok')
plt.xlim(lim_plot[0, 0], lim_plot[0, 1])
plt.ylim(lim_plot[1, 0], lim_plot[1, 1])
plt.xlabel('x')
plt.ylabel('y')

plt.show()
plt.close('all')
