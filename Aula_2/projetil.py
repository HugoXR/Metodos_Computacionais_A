"""
Created on Wed Nov 24 16:30:36 2021

@author: Hugo X Rodrigues
"""

#Grafico da trajetoria de um projetil sem atrito com o ar
import math as m
import matplotlib.pyplot as plt

#Definindo as velocidades e posicoes iniciais
x_0, y_0 = 0, 0
vx_0, vy_0 = 10, 20

#Aceleracao da gravidade
g = -10

#Calculo do tempo necessario para o projetil voltar ao solo
t_f = -(2*vy_0)/g
delta_t = t_f/20

#Definir a lista t, com valores entre 0 e tf e intervalos delta_t
t = [time*delta_t for time in range(21)]

#Definir as listas x com a posicao horizontal da particula para cada valor de t
x = [x_0+vx_0*t_x for t_x in t]

#Definir as listas y com a posicao horizontal da particula para cada valor de t
y = [y_0+vy_0*t_y+(g*t_y**2)/2 for t_y in t]

#Faca o grafico da trajetoria da particula, y por x
plt.plot(x, y, "--o")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("Trajetoria_projetil.pdf")
plt.show()
