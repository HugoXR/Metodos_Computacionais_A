# Prova 1 - Questão 1 - Metodos Computacionais A
import numpy as np
import matplotlib.pyplot as plt

# Autor: Hugo Xavier Rodrigues
# Matricula: 190108622
# Data: 08/03/2022
# Objetivo: Realizar um programa que calcule as potências solares incidentes ao
# longo do ano conforme orientado na questão 1 da prova


print("Autor: Hugo Xavier Rodrigues")
print("Matricula: 190108622")
print("Data: 08/03/2022")
print("Objetivo: Realizar um programa que calcule as potencias solares incident"
      +"es ao longo do ano conforme orientado na questao 1 da prova")
print("\n\n")

dias = np.arange(0, 365) # Quantidade de dias do ano

# Dias restantes para o fim do ano partindo do solsiticio
dias_do_solsticio_para_fim_ano = 9

# Dia do solsticio
dia_solsticio = dias[-1] - dias_do_solsticio_para_fim_ano

# Dias transcorridos entre o solsticio e os dias do ano
N_dias = np.zeros(len(dias))
N_dias[:dia_solsticio] = 9 + 1 + dias[:dia_solsticio]
N_dias[dia_solsticio:] = (dias[dia_solsticio:] - dia_solsticio)

# Latitude de brasilia
alpha =  np.radians(-15.8)

# Angulo da Ecliptica
beta = np.radians(23.44)

# Angulo de culminacao - Angulo entre o Sol e a direcao vertical de determinado ponto da Terra 
theta_cul = -beta*np.cos(2*np.pi*N_dias/365) - alpha

# Angulo de culminacao em graus
theta_cul_degree = np.degrees(theta_cul)


# Grafico do Angulo de cuminacao em cada dia do ano
plt.plot(dias, theta_cul_degree, label="Angulo de culminacao")
plt.title("Angulo de culminacao por dia")
plt.xlabel("Dia do ano")
plt.ylabel("Angulo de Cuminação em $\\degree$")
plt.savefig("Angulo_Dia.pdf")
plt.legend()
plt.show()
plt.close("all")

# Intensidade da radiacao solar em W/m^2
Intensidade = 1000

# Area m^2
A = 1

# Potencia Solar
potSolar = Intensidade*A*np.cos(theta_cul)

# Energia potencial anual media
potMean = np.mean(potSolar)

# Angulos da placa com a horizontal
alpha = np.arange(-30, 31)

theta_cul_alpha_degree = np.zeros(shape=(len(alpha), len(theta_cul)))

# Angulo de culminacao em graus com a placa sob angulo alpha com a horizontal
for i, angulo in enumerate(alpha):
    theta_cul_alpha_degree[i] = theta_cul_degree - angulo 

# Angulo de culminacao em radianos com a placa sob o anuglo alpha com a horizontal
theta_cul_alpha = np.radians(theta_cul_alpha_degree)

# Potencia Solar com a placa sob angulo alpha
potSolar_alpha = Intensidade*A*np.cos(theta_cul_alpha)

# Potencia solar com a placa sob angulo alpha media
potMean_alpha = np.mean(potSolar_alpha, axis=1)


print("Angulos de alpha(em graus) \t Potencia Media (em Watts)")
for i, angulo in enumerate(alpha):
    print(f"{angulo} \t\t\t\t {potMean_alpha[i]}")

potMean_max_indice = np.argmax(potMean_alpha)

max_PotSolar = potSolar_alpha[potMean_max_indice]
max_alpha_degree = alpha[potMean_max_indice]

# Grafico da potencia solar incidente por ano, com alpha = 0 e alpha maximo
plt.plot(dias, potSolar, label="potencia solar $\\alpha = 0\\degree$")
plt.plot(dias, max_PotSolar, label="potencia solar $\\alpha$ = "
         +f"{max_alpha_degree} $\\degree$")
plt.xlabel("Dias do ano")
plt.ylabel("Potencia Solar (W)")
plt.title("Potencia Solar ao longo do ano")
plt.legend()
plt.savefig("Potencia_Solar_Ano.pdf")
plt.show()
plt.close("all")
