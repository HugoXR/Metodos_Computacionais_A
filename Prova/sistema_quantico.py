# Prova 1 - Questão 2 - Metodos Computacionais A
import numpy as np

# Autor: Hugo Xavier Rodrigues
# Matricula: 190108622
# Data: 08/03/2022
# Objetivo: Realizar um programa que calcule os estados e energias de um
# sistema quântico conforme orientado na questão 2 da prova

print("Autor: Hugo Xavier Rodrigues")
print("Matricula: 190108622")
print("Data: 08/03/2022")
print("Objetivo: Realizar um programa que calcule os estados e energias de "
      +"um sistema quantico conforme orientado na questao 2 da prova")
print("\n\n")


# Operador hamiltoniano
H = np.array([[3, 1+1j, 1, 0], [1-1j, 4, 0, 2], [1, 0, 4, -1j], [0, 2, 1j, 1]])

# E - Autovalores de Energia, psi - autoestados do sistema 
E, psi = np.linalg.eig(H)

# Produto dos autovalores de Energia pelos autoestados do sisitema
E_psi = np.zeros_like(psi)
for i, value in enumerate(E):
    E_psi[:, i] = value*psi[:, i]

# Produto do Operador hamiltoniano pelos autoestados do sistema
H_psi = np.dot(H, psi)

if(np.max(abs(E_psi - H_psi)) < 1E10-15):
    print("A equacao do sistema quantico é obedecida para os autovalores de"
          +" Energia:\n", E, "\nE os autoestados do sistema:\n", psi,"\n\n")
    for i, autovalor_Energia in enumerate(E):
        print(f"{i} {autovalor_Energia}\n{np.reshape(psi[:, i], (len(psi[:, i]), 1))}")
        print(f"Autovetor e autovalor corretos\n")




