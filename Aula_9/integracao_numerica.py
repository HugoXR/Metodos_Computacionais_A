import numpy as np
import matplotlib.pyplot as plt
import time

def f(x):
    return np.exp(x)


def primitiva_f(x):
    return np.exp(x)


a = 5
b = 10

intAlgebrica = primitiva_f(b) - primitiva_f(a)

N = np.logspace(1,3,100).astype(int)

def integral_trapezio(a, b, f, N):
    x = np.linspace(a, b, N)

    del_X = (b-a)/(N-1)
    f_x = f(x)

    intNumerica = del_X*(f_x[0]*0.5 + f_x[1:-1].sum() + f_x[-1]*0.5)
    return intNumerica

intNumerica = integral_trapezio(a, b, f, N[-1])

print(f"Integral algebrica: {intAlgebrica}")
print(f"Integral Numerica: {intNumerica}")


intNumerica_N = [integral_trapezio(a, b, f, n) for n in N]

plt.plot(N, abs(intNumerica_N - intAlgebrica), '-o')
plt.loglog()
plt.xlabel("Numero de pontos")
plt.ylabel("Erro Numerico")
plt.show()

