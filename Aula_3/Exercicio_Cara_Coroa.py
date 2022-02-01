# Exercicio para determinar a chance de uma moeda cair 10 caras em 1000000
# tentativas a cada 10

import numpy as np

lances_1 = np.array([])
caras_10 = 0
N = 1000000

# Iterando 1000000 para determinar se houve 10 caras nas 10 tentativas
for i in range(N):
    lances_1 = (np.random.uniform(size=10) < 0.5).sum()
    if lances_1 == 10:
        # Acrescentando a quantidade de vezes em que deu cara 10 vezes
        caras_10 += 1

# caras_10 = (((((np.random.uniform(size=[10, N])) > 0.5).sum(axis=0)) == 10)
# .sum())

print("A chance de da 10 caras em 1000000 de tentativas e "+
      f"{(caras_10/N)*100:.4f}%")
