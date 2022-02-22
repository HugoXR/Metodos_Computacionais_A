# Solucao do sistema linear de um circuito eletrico
import numpy as np

# Solucao sistema de somente as malhas com I7, I8 e I6
C1 = np.loadtxt("matriz_circuito_I6_I7_I8.dat", max_rows=1)
C1 = C1.reshape([C1.size, 1])
A1 = np.loadtxt("matriz_circuito_I6_I7_I8.dat", skiprows=1)

B1 = np.linalg.solve(A1, C1)

erro = np.abs(np.dot(A1, B1) - C1)

if all(erro) < 1e-11:
    print(f"Os valores das correntes para somente I6, I7 e I8 sao\nI6={B1[0,0]}A\nI7={B1[1,0]}A\nI8={B1[2,0]}A")
else:
    print("Erro ao encontrar solucao do sistema")

# Solucao sistema completo sem considerar as 2 resistencia de 1ohm
C2 = np.loadtxt("matriz_circuito.dat", max_rows=1)
C2 = C2.reshape([C2.size, 1])
A2 = np.loadtxt("matriz_circuito.dat", skiprows=1)

B2 = np.linalg.solve(A2, C2)

erro = np.abs(np.dot(A2, B2) - C2)

if all(erro) < 1e-11:
    print(f"\nOs valores das correntes para o circuito completo sao\nI1={B2[0,0]:.3f}A\nI2={B2[1,0]:.3f}A\nI3={B2[2,0]:.3f}A\nI4={B2[3,0]:.3f}A"+
             f"\nI5={B2[4,0]:.3f}A\nI6={B2[5,0]:.3f}A\nI7={B2[6,0]:.3f}A\nI8={B2[7,0]:.3f}A")
else:
    print("Erro ao encontrar solucao do sistema")


# Solucao sistema com somente as malhas superiores
C3 = np.loadtxt("matriz_circuito.dat", max_rows=1)
C3 = C3.reshape([C3.size, 1])
A3 = np.loadtxt("matriz_circuito.dat", skiprows=1)

B3 = np.linalg.solve(A3, C3)

erro = np.abs(np.dot(A3, B3) - C3)

if all(erro) < 1e-11:
       print(f"\nOs valores das correntes somente das malhas superiores sao\nI1={B3[0,0]:.3f}A\nI2={B3[1,0]:.3f}A\nI3={B3[2,0]:.3f}A\nI4={B3[3,0]:.3f}A"+
             f"\nI5={B3[4,0]:.3f}A")
else:
    print("Erro ao encontrar solucao do sistema")

# Solucao sistema considerando os resitores de 1 ohm
C = np.loadtxt("matriz_circuito_2.dat", max_rows=1)
C = C.reshape([C.size, 1])
A = np.loadtxt("matriz_circuito_2.dat", skiprows=1)

B = np.linalg.solve(A, C)

erro = np.abs(np.dot(A, B) - C)

if all(erro) < 1e-11:
    print(f"\nOs valores das correntes para o circuito completo com os resitores de 1 ohm sao\nI1={B[0,0]:.3f}A\n"+
          f"I2={B[1,0]:.3f}A\nI3={B[2,0]:.3f}A\nI4={B[3,0]:.3f}A"+
          f"\nI5={B[4,0]:.3f}A\nI6={B[5,0]:.3f}A\nI7={B[6,0]:.3f}A\nI8={B[7,0]:.3f}A")
else:
    print("Erro ao encontrar solucao do sistema")

