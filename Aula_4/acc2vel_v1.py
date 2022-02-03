import numpy as np
import matplotlib.pyplot as plt

# Valores de Entrada
del_T = 0.1
aceleracao = np.loadtxt('acc.dat')
k = len(aceleracao)
tempo = np.arange(k)*del_T

# Calculo da Velocidade
velocidade = np.zeros_like(aceleracao)
velocidade[0] = 0
velocidade[1:] = [del_T*(0.5*(aceleracao[0]+aceleracao[i])+aceleracao[1:i].sum()) for i in range(1, k)]

# for i in range(1, k):
#    vel[i] = del_T*(0.5*(aceleracao[0]+aceleracao[i])+aceleracao[1:i].sum())

# Gerando Grafico
plt.plot(tempo, aceleracao, 'b')
plt.plot(tempo, velocidade, 'r')
plt.legend(['Aceleracao (m/s$^2$)', 'Velocidade (m/s)'])
plt.xlabel("Tempo (s)")
plt.savefig('aceleracao.pdf')
plt.close('all')
