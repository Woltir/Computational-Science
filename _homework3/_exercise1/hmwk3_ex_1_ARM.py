import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random, seed


def Distribution(n_item) :          # Generate a random discrete distribution of n_item
    seed=(1234)                     # elements
    r = random(size=(n_item))       # i. Generation of n_item numbers
    Z = np.sum(r)                   # ii. Computation of normalization constant 
    print('Z=',Z)                   #
    p = r/Z                         # Normalization
    print('sum over p = ',np.sum(p)) # Verification 
    return(p)

def AcceptRejectMethod(N,p) :       # Generate random numbers w.r.t the distribution p
    X = random(size=(2,N))*np.size(p) ; I = X[0].astype(int) 
                                    # Generation of 2N r.n. (X,Y)
                                    # I is the int part of X in order to have a discrete r.n.
    Z = (X[1]<p[I]*np.size(p),I)    # Z include boolean and int. c.f. Marin
    P = np.argsort(np.unique(Z[1])) # Creation of a vector [i_1, i_2, ***, i_n]

    print(I)                        # Show the r.n. to serif with eyes
    h=np.zeros((np.size(p),2), dtype='int') # Array of result
    for i in P :                            # 1st col : i_i
        h[i]=i,np.sum(Z[1]*1==i)            # 2nd col : nb. of i
    print(h)



