import numpy as np
import matplotlib.pyplot as plt

N = 9 
k = 5
m = 0.1

k_m = k/m

A = np.zeros([N, N])

# Condicao de contorno extremidades fixas
np.fill_diagonal(A, 2*k_m)
A += np.diag(-k_m*np.ones(N-1), 1) + np.diag(-k_m*np.ones(N-1), -1)

autovalores, autovetores = np.linalg.eig(A)

X_0 = np.zeros([N, 1])
X_0[0] = 0.01

b_n = np.dot(autovetores.T, X_0)
x_t = []
x = 0
t = np.arange(0, 2, 0.1)
omega = np.sqrt(autovalores).reshape((N, 1))

x_t = np.dot(autovetores, b_n * np.cos(omega * t))

fig = plt.figure()
grap1 = fig.add_subplot(2, 1, 1)
for i, value in enumerate(x_t):
    plt.plot(t, value, label=f"{i}")
plt.legend()
plt.title("Grafico X(t)")

grap2 = fig.add_subplot(2, 1, 2)
iN = np.arange(N)
for i in iN:
    plt.plot(iN, iN*0+i, '-', color='gray')
    plt.plot(iN, autovetores[:, i]+i, '-', label=f"{i}")
plt.legend()
plt.title("Grafico Modos Normais")
plt.show()
