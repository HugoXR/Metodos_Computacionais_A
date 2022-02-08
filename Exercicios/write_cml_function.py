import numpy as np
from scitools.StringFunction import StringFunction

# Lendo a funcao f, os intervalos [a,b] e a quantidade de valores n
f, a, b, n = np.loadtxt("write_func.dat", dtype=str , delimiter=',')
a = int(a)
b = int(b)
n = int(n)


interval = np.linspace(a, b, n) # Intervalo dos x
func = StringFunction(f) # declaracao da funcao
func_vec = np.vectorize(func) # Permitindo a vetorizacao
f_x = np.array(func_vec(interval)) # Funcao aplicada para cada valor de x

output_array = np.stack((interval, f_x), axis=1) # Array para saida dos dados

#Escrevendo os dados no arquivo output.dat
with open("output.dat", "w") as file:
    for row in output_array:
        for column in row:
          file.write(f"{column:.2f}\t")
        file.write('\n')
