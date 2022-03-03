# Calculo do de autovetor e autovalor de um sistema massa-mola AX = lambdaX
import numpy as np
import matplotlib.pyplot as plt


N = 10
iN = np.arange(N)
k_m = 1 # k/m

# construcao da matriz evolucao temporal
A = np.zeros([N, N])

np.fill_diagonal(A, 2*k_m) # Equiv A[i, i] = 2*k_m

# A = A + np.diag(-np.ones(4)*km,1) + np.diag(-np.ones(4)*km,-1)
# Condicao de contorno extremindades livres
# A[0, 0] = A[-1, -1] = k_m
A[iN[1:], iN[:-1]] = -k_m
A[iN[:-1], iN[1:]] = -k_m

# Condicao de contorno periodica
A[0, -1] = A[-1, 0] = -k_m

# impureza na rede (massa 5 mais pesada)
A[N//2, :] /= 50

# Calculo dos autovalores e autovetores
autovalores, autovetores = np.linalg.eig(A)
# ordenando autovalor
asort = np.argsort(autovalores)
autovalores = autovalores[asort]
autovalores[autovalores < 0] = 0
# ordenando autovetor
# autovetores = autovetores[:, asort]

print("Autovalores: ", autovalores)
print("autovetores: ", autovetores)

omega = np.sqrt(autovalores) # Frequencias

fig = plt.figure()
graf1 = fig.add_subplot(2, 1, 1)
# Grafico das frequencias (energias=hf)
plt.plot(iN, omega, 'o')
plt.ylabel('Omega')
plt.xlabel('Numero do autovalor')

# Grafico dos modos normais
graf2 = fig.add_subplot(2, 1, 2)
for i in iN:
    plt.plot(iN, iN*0+i, '-', color='gray')
    plt.plot(iN, autovetores[:, i]+i, '-')

plt.show()

