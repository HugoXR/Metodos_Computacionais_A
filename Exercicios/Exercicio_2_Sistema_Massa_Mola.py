import numpy as np
import matplotlib.pyplot as plt

N = 9
k = 5
m = 0.1

k_m = k/m

A = np.zeros([N,N])
np.fill_diagonal(A, 2*k_m)
A += np.diag(-k_m*np.ones(N-1),1) + np.diag(-k_m*np.ones(N-1),-1)
autovalores, autovetores = np.linalg.eig(A)

X_0 = np.zeros([N, 1])
X_0[0] = 0.01

b_n = np.dot(autovetores.T,X_0)
