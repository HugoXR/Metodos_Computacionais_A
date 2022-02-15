#Solucao do sistema linear com inverso da matriz A
import numpy as np
import time

N = 100
A = np.random.uniform(size=[N, N])
C   = np.random.uniform(size=[N, 1])
t0 = time.time()
B = np.dot(np.linalg.inv(A), C)
t1 = time.time()
erro = np.abs(np.dot(A, B) - C)
if(all(erro < 1e-10)):
    print("A solocao do sistema é: \nB:\n",B)
else:
    print("Solucao errada")
print(f"O tempo de calculo é : {t1 - t0:.4f}")
print(f"Erro medio é {erro.mean()}")
