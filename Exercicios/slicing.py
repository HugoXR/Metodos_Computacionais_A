import numpy as np

w = np.arange(0,3.1,0.1)

print(f"Todos os elementos do array w: {w[:]}") # [0, 0.1, 0.2, ..., 3.0]
print(f"Elementos do array w menos os 2 últimos:  {w[:-2]}") # [0, 0.1, 0.2, ..., 2.8]
print(f"Elementos multiplos de 0.5 do array w: {w[::5]}") # [0, 0.5, 1, 1.5, 2.0, 2.5, 3.0]
print(f"Elementos do array w do segundo ao antipenultimo elemento, pulando de 6 em 6 elementos: {w[2:-2:6]}") # [0.2, 0.8, 1.4, 2.0, 2.6]
