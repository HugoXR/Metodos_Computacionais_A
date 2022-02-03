import numpy as np
import matplotlib.pyplot as plt


# Parametros do movimento oscilatorio amortecido
periodo = 1
amplitude = 0.2
tau = 3*periodo # x = amplitude * cos(t*2*pi/periodo) * exp(-t/tau), 2*pi/periodo = w
erro = 0.05

# Curvas Teoricas
tempo = np.linspace(0, 3*periodo, 300)
x_teorico = amplitude * np.cos(tempo*2*np.pi/periodo) * np.exp(-tempo/tau)

# Pontos experimentais
tempo_exp = np.arange(0, 3*periodo, 0.1)
x_exp = amplitude * np.cos(tempo_exp*2*np.pi/periodo) * np.exp(-tempo_exp/tau)
error = np.random.uniform(-erro, erro, len(x_exp))
x_exp += error

# Grafico
plt.title('Pêndulo Amortecido')
# plt.plot(tempo_exp, x_exp+0.01, 'r')
plt.errorbar(tempo_exp, x_exp, erro, fmt='ro', label='Experimental')
plt.plot(tempo, x_teorico, '-b', label='Teórico')
plt.legend()
plt.xlim(0, 3) # Limitando o tempo de 0 a 3s
plt.ylim(-amplitude, amplitude)
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.savefig('Oscilador_T.pdf')
plt.close('all')
