import numpy as np
from scipy.sparse import csc_matrix

def pageRank(G, maxerr):

    n = G.shape[0]
    s = .85
    # transform G into markov matrix A
    A = csc_matrix(G, dtype=np.float)
    # number of 1s in a row in G matrix
    rsums = np.array(A.sum(1))[:, 0]
    # Return the indices of the elements that are non-zero.
    ri, ci = A.nonzero()
    A.data /= rsums[ri]
    #print(A.todense())
    # bool array of sink states
    sink = rsums == 0
    # Compute pagerank r until we converge
    ro, r = np.zeros(n), np.ones(n)
    while np.sum(np.abs(r-ro)) > maxerr:
        ro = r.copy()
        # calculate each pagerank at a time
        for i in range(0, n):
            # inlinks of state i
            Ai = np.array(A[:, i].todense())[:, 0]
            # account for sink states
            Di = sink / float(n)
            # account for teleportation to state i
            Ei = np.ones(n) / float(n)
            r[i] = ro.dot(Ai*s + Di*s + Ei*(1-s))


    # return normalized pagerank
    return r/float(sum(r))




if __name__=='__main__':
    '''
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
    
    G = np.array([[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    '''
    G = np.array([[0, 1, 1, 0],
                  [0, 0, 0, 1],
                  [1, 1, 0, 1],
                  [1, 0, 0, 0]])

    print(pageRank(G, maxerr=.1))
