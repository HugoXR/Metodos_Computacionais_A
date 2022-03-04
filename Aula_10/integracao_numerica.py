# Metodo do trapezio iterativo
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


N = np.logspace(1, 3, 100).astype(int)


def integral_trapezio(a, b, f, N=None, erro=None):
    # Calcula a funcao nos limites de integracao
    f_ab = (f(a)+f(b))/2

    # Calcula a integral com numero de pontos fixo
    if N is not None:
        x = np.linspace(a, b, N)
        del_X = (b-a)/(N-1)
        f_x = f(x)
        intNumerica = del_X*(f_ab + f_x[1:-1].sum())
        return intNumerica
    # Calcula a integral ate determinado e2ddrro
    else:
        erroAtual = 1e10
        exp2 = 1
        somaCentro = f((a+b)/2)
        intAtual = (f_ab + somaCentro)*((b - a)/2)
        while erroAtual > erro:
            exp2 += 1
            if(exp2 > 28):
                print('Erro: calculo nao converge')
                os.sys.exit()
            M = 2**exp2
            x = np.linspace(a, b, M+1)
            somaCentro += f(x[1::2]).sum()
            intAnterior = intAtual
            intAtual = (f_ab + somaCentro)*((b - a)/M)
            erroAtual = abs(intAtual - intAnterior)
            print(exp2, M, erroAtual, intAtual)
        return intAtual


erro = 1e-10

# print(f"Integral algebrica: {intAlgebrica}")
# print(f"Integral Numerica: {intNumerica}")
# plt.plot(N, abs(intNumerica_N - intAlgebrica), '-o')
# plt.loglog()
# plt.xlabel("Numero de pontos")
# plt.ylabel("Erro Numerico")
# plt.show()

