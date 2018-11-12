import numpy as np
from scipy.sparse import csc_matrix

d = 0.85
s = 1 - d
eps = 1.0e-8

def to_markov(G):
    A = csc_matrix(G, dtype=np.float)
    col_sum = np.array(A.sum(1))[:, 0]
    A = A.todense()
    n = A.shape[1]
    for i in range(0, n):
        if col_sum[i] == 0:
            A[i] = 1 / n
        else:
            A[i] /= col_sum[i]
    return A.transpose()

def pageRank(G):
    G = to_markov(G)
    n = G.shape[1]
    v = np.random.rand(n, 1)
    v /= np.linalg.norm(v, 1)
    # we craete this vector just for the first test in while loop
    v_p = np.ones((n, 1), dtype=np.float32) * 100
    H = (d * G) + (((1 - d) / n) * np.ones((n, n), dtype=np.float32))

    #while np.linalg.norm(v - v_p, 2) > eps:
    v_t = v
    while sum(np.abs(v_t - v_p)) > eps:
        v_p = v_t
        v_t = np.matmul(H, v_t)
    return v_t


G = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]])


print(pageRank(G)*100)
