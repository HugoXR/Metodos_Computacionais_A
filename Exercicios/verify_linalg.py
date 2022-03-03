import numpy as np

N = 4
A = np.random.randint(10, size=[N, N])
B = np.random.randint(10, size=[N, N])
C = np.random.randint(10, size=[N, N])

def distrib(A, B, C):
    result1 = (A + B)@C
    result2 = A@C + B@C

    err = 1E-14
    assert abs(result1 - result2).max() < err

def assoc(A, B, C):
    result1 = (A@B)@C
    result2 = A@(B@C)

    err = 1E-14
    assert abs(result1 - result2).max() < err

def rank_transp(A):
    result1 = np.linalg.matrix_rank(A)
    result2 = np.linalg.matrix_rank(A.T)

    err = 1E-14
    assert abs(result1 - result2) < err

def det_prod(A, B):
    result1 = np.linalg.det(A@B)
    result2 = np.linalg.det(A)*np.linalg.det(B)

    err = 1E-8
    assert abs(result1 - result2) < err

def eigenvalues_transp(A):
    result1 = np.linalg.eigvals(A)
    result2 = np.linalg.eigvals(A.T)

    err = 1E-8
    assert abs(result1 - result2).max() < err

distrib(A, B, C)
assoc(A, B, C)
rank_transp(A)
det_prod(A, B)
eigenvalues_transp(A)


