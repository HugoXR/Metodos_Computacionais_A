# Problema lançamento obliquo com arrasto - Metodo de Euler
import numpy as np
import matplotlib.pyplot as plt

C = 1
m = 1
v_Vento = np.array([10., 0.])
g = 9.82
r0 = np.array([0., 0.])
v0 = np.array([10., 10.])
del_t = 0.001


def f(X, t):
    vr = X[2:]-v_Vento
    modulo_vr = np.linalg.norm(vr) # vr**2.sum()**0.5
    return np.array([X[2], X[3], -C/m*modulo_vr*vr[0], -C/m*modulo_vr*vr[1] - g])


t = 0.
X = np.concatenate([r0, v0])
trajetoria = np.concatenate([[t], X])


while X[1] >= 0:
    X += f(X, t)*del_t
    t += del_t
    trajetoria = np.vstack([trajetoria, np.concatenate([[t], X])])

plt.subplot(2, 3, 1)
plt.plot(trajetoria[:, 0], trajetoria[:, 1])
plt.xlabel('$t$')
plt.ylabel('$x$')

plt.subplot(2, 3, 4)
plt.plot(trajetoria[:, 0], trajetoria[:, 2])
plt.xlabel('$t$')
plt.ylabel('$y$')

plt.subplot(2, 3, 2)
plt.plot(trajetoria[:, 0], trajetoria[:, 3])
plt.xlabel('$t$')
plt.ylabel('$v_{x}$')

plt.subplot(2, 3, 5)
plt.plot(trajetoria[:, 0], trajetoria[:, 4])
plt.xlabel('$t$')
plt.ylabel('$v_{y}$')

plt.subplot(2, 3, 3)
plt.plot(trajetoria[:, 1], trajetoria[:, 2])
plt.xlabel('$x$')
plt.ylabel('$y$')


plt.show()
