import numpy as np
import matplotlib.pyplot as plt


# Parametros do movimento oscilatorio amortecido
periodo = 1
amplitude = 0.2
tau = 3*periodo # x = amplitude * cos(t*2*pi/periodo) * exp(-t/tau), 2*pi/periodo = w
erro = 0.02

# Curvas Teoricas
omega = 2*np.pi/periodo
tempo = np.linspace(0, 3*periodo, 300)
x_teorico = amplitude * np.cos(tempo*omega) * np.exp(-tempo/tau)
v_teorico = -amplitude*(omega*np.sin(omega*tempo) +
             (1/tau)*np.cos(omega*tempo))*np.exp(-tempo/tau)


# Pontos experimentais
tempo_exp = np.arange(0, 3*periodo, 0.1)
x_exp = amplitude * np.cos(tempo_exp*omega) * np.exp(-tempo_exp/tau)
error = np.random.uniform(-erro, erro, len(x_exp))
x_exp += error

# Calculo da Velocidade
v_exp = (x_exp[1:] - x_exp[:-1]) / (tempo_exp[1:] - tempo_exp[:-1])
tv_exp = (tempo_exp[:-1]+tempo_exp[1:])/2

# Grafico da posicao
# plt.plot(tempo_exp, x_exp+0.01, 'r')
plt.errorbar(tempo_exp, x_exp, erro, fmt='ro', label='$x_{exp}$')
plt.plot(tempo, x_teorico, '-r', label='$x_{teo}$')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)', color='r')
plt.plot(tempo, amplitude*np.exp(-tempo/tau), ':', color="gray")
plt.plot(tempo, -amplitude*np.exp(-tempo/tau), ':', color="gray")
plt.legend(bbox_to_anchor=(0.83, 0.165))
plt.ylim(-amplitude, amplitude)
plt.xlim(0, 3) # Limitando o tempo de 0 a 3s

# Grafico da velocidade
plt.twinx()
plt.plot(tv_exp, v_exp, 'sb', label='$v_{exp}$')
plt.plot(tempo, v_teorico, '--b', label='$v_{teo}$')
plt.ylim(-omega*amplitude, omega*amplitude)
plt.ylabel('Velocidade (m/s)', color='b')
plt.legend(loc='lower right')

# Comando Grafico
plt.text(0.7, 0.8, '$x_{teo} = A\\cos{(\\omega t)}e^{\\frac{-T}{\\tau}}$\n$A=$'
         +'%.1fm\n$T =$%.1fs\n$\\tau = $%.2fs' %(amplitude, periodo, tau), transform=plt.gca().transAxes)
plt.title('Pêndulo Amortecido')
plt.savefig('Oscilador_T.pdf')
plt.close('all')
