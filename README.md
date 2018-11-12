# Page-Rank
Google search algorithm


Create a transition matrix:
Aij = 1 if there is a transition from page Ai to page Aj
      0 if not

i used Google exemple: https://en.wikipedia.org/wiki/PageRank#/media/File:PageRanks-Example.jpg

              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
              [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
              [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]
              [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]
              [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]
              [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]
              [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
             
to_markov() function generate the stochastic matrix (probability distribution)
