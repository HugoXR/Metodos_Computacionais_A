# Solucao de um sistema linear qualquer
import numpy as np

C = np.loadtxt("matriz.dat", max_rows=1)
C = C.reshape([C.size, 1])
A = np.loadtxt("matriz.dat", skiprows=1)

B = np.linalg.solve(A, C)

erro = np.abs(np.dot(A, B) - C)

if all(erro) < 1e-11:
    print(f"O valor da solucao do sistema linear e: \nB=\n{B}")
else:
    print("Erro ao encontrar solucao do sistema")
