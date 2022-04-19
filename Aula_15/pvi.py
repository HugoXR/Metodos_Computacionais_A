# Problema lançamento obliquo com arrasto - Metodo de Euler e Runge-Kutta
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

C = 1
m = 1
v_Vento = np.array([0., 0.])
g = 10
r0 = np.array([0., 0.])
v0 = np.array([7., 7.])
del_t = 0.001
tFinal = 0.8


def f(X, t):
    vr = X[2:]-v_Vento
    modulo_vr = np.linalg.norm(vr) # vr**2.sum()**0.5
    return np.array([X[2], X[3], -C/m*modulo_vr*vr[0], -C/m*modulo_vr*vr[1] - g])

# Metodo de Euler
X_final = np.zeros([0, 5])
for delt in np.logspace(-4, -1, 9):
    t = 0.
    X = np.concatenate([r0, v0])
    trajetoria = np.concatenate([[t], X])

    while t < tFinal:
        X += f(X, t)*delt
        t += delt
        trajetoria = np.vstack([trajetoria, np.concatenate([[t], X])])
    X_final = np.vstack([X_final, np.concatenate([[delt], X])])


# Grafico do erro metodo de euler em relacao ao delta t
erro = np.abs(X_final[:, 1:]-X_final[0, 1:]).sum(axis=1)
plt.plot(X_final[1:, 0], erro[1:], '-o', label='Erro Euler')

X = 0
X_final = np.zeros([0, 5])
tFinal = 0.8

# Metodo de Runge-Kutta
for delt in np.logspace(-6, -1, 6):
    t = 0.
    X = np.concatenate([r0, v0])
    trajetoria = np.concatenate([[t], X])

    while t+delt/2 < tFinal:
        X += f(X+f(X, t)*delt/2, t+delt/2)*delt
        t += delt
    print(delt, t)
    X_final = np.vstack([X_final, np.concatenate([[delt], X])])

# Grafico do erro metodo de runge-kutta em relacao ao delta t
erro = np.abs(X_final[:, 1:]-X_final[0, 1:]).sum(axis=1)
plt.plot(X_final[1:, 0], erro[1:], '-o', label='Erro Runge-Kutta')
plt.plot(X_final[:, 0], 10*X_final[:, 0], label="$\Delta t^1$")
plt.plot(X_final[:, 0], 50*X_final[:, 0]**2, label="$\Delta t^2$")
plt.loglog()
plt.xlabel('$\Delta t$')
plt.ylabel('Erro')
plt.legend()
plt.show()
plt.close()

# Metodo de Runge Kutta de 4 ordem, atraves do odeint
t = np.linspace(0, tFinal, 100)
X0 = np.concatenate([r0, v0])
trajetoria = odeint(f, X0, t)
trajetoria = np.hstack([t.reshape(len(t), 1), trajetoria])

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
plt.close()

