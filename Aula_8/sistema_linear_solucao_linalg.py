# Solucao de um sistema linear qualquer
import numpy as np
import time

N = 100
A = np.random.uniform(size=[N, N])
C = np.random.uniform(size=[N, 1])

t0 = time.time()
B = np.linalg.solve(A, C)
det = np.linalg.det(A)
t1 = time.time()

erro = np.abs(np.dot(A, B) - C)

if all(erro) < 1e-11:
    print(f"O valor da solucao do sistema linear e: \nB=\n{B}")
else:
    print("Erro ao encontrar solucao do sistema")

print(f"A determinante da matriz A é : {det:.3f}")
print(f"O tempo necessario para os calculos foi: {t1-t0:.4f}")
print(f"O erro medio é de {erro.mean()}")
