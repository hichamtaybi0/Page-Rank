from scipy.sparse import csc_matrix
import numpy as np
import networkx as nx

d = 0.85
s = 1 - d
eps = .0001
file = 'graph.xml'

'''
graph2matrix() creates the transition matrix,
Aij = 1 if there is a transition from page Ai to page Aj, 0 if not
'''
def graph2matrix(file):
    graph = nx.read_graphml(file)
    matrix = nx.to_numpy_matrix(graph)
    return matrix

'''
to_markov() takes transition matrix as input and generates the stochastic matrix (probability distribution)
'''
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
    M = graph2matrix(G)
    T = to_markov(M)
    n = T.shape[1]
    v = np.random.rand(n, 1)
    v /= np.linalg.norm(v, 1)
    v_p = np.ones((n, 1), dtype=np.float32) * 100  # this vector just for the first test in while loop
    H = (d * T) + (((1 - d) / n) * np.ones((n, n), dtype=np.float32))
    v_t = v
    while sum(np.abs(v_t - v_p)) > eps:
        v_p = v_t
        v_t = np.matmul(H, v_t)
    return v_t



if __name__ == '__main__':
    R = pageRank(file)
    print(R)
