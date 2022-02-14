import numpy as np

A = np.array([[3., 5., 0.], [2., 0., 1.], [5., 1., -1.]])
C = np.array([1., 3., 0.])

# C = np.loadtxt("matriz.dat", max_rows=1)
# A = np.loadtxt("matriz.dat", skiprows=1)


def resolveSL(A, C):
    """
    Resolve um sistema linear AB = C
    Parametros
    ------------
    A: Matriz de coeficientes NxN
    C: Matriz de constantes Nx1
    Retorna
    ------------
    A matriz B, solucao do sistema linear
    """
    if(A.shape[1] != C.shape[0]):
        raise TypeError("Tamanhos das matrizes A e C distintos")
    N = A.shape[0]
    for i in range(N):
        j = np.argmax(abs(A[:, i])) # retorna o indice do maior elemento
        if(j > i):
            # Trocando as linhas
            linha_i = A[i, :].copy()
            A[i, :] = A[j, :]
            A[j, :] = linha_i
            # Trocando as linhas
            linha_i = C[i].copy()
            C[i] = C[j]
            C[j] = linha_i
        for k in range(N):
            if(i != k and A[i, i] != 0):
                C[k] = C[k].copy() - (((C[i]/A[i, i])*A[k, i])).copy()
                A[k, :] = A[k, :].copy() - (((A[i, :]/A[i, i]))*(A[k, i])).copy()
        B = A.diagonal()
    return B


B = resolveSL(A, C)
print(B)
