# Metodo do Simpson
import numpy as np
import matplotlib.pyplot as plt
import time
import os


def f(x):
    return np.exp(x)


def primitiva_f(x):
    return np.exp(x)


# Limites de integração
a = 5
b = 10


# Valor Algebrico
intAlgebrica = primitiva_f(b) - primitiva_f(a)


N = np.logspace(1, 15, 15, base=2).astype(int)+1


def integral_simpson(a, b, f, N):
    if N % 2 != 1:
        print("N deve ser impar")
        os.sys.exit()
    # Calcula a funcao nos limites de integracao
    f_ab = f(a)+f(b)
    x = np.linspace(a, b, N)
    del_X = (b-a)/(N-1)
    f_x = f(x)
    intNumerica = (del_X/3)*(f_ab + 4*f_x[1:-1:2].sum()+2*f_x[2:-1:2].sum())
    return intNumerica


intSimpson = np.array([integral_simpson(a, b, f, n) for n in N])
erro = 1e-10

# print(f"Integral algebrica: {intAlgebrica}")
# print(f"Integral Numerica: {intNumerica}")
plt.plot(N, abs(intSimpson - intAlgebrica), '-or', label="Integral Simpson")
plt.plot(N, 1e5*N**-4., '--r', label='potencia -4')
plt.loglog()
plt.xlabel("Numero de pontos")
plt.ylabel("Erro Numerico")
plt.legend()
plt.show()

