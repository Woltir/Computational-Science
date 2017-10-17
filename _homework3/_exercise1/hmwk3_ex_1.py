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

def TowerSampling(N,p) :            # Generate random numbers w.r.t the distribution p
    C = np.cumsum(p)*np.size(p)     # Creation of the cumulative
    print('C_n =',C[-1])            # Verification 
    Y = random(size=(N))*np.size(p) # Generate N r.n. 
    Z = np.zeros((2,np.size(p)))    # Creation of a vector where put results
    Z[0] = np.arange(np.size(p))    # Just indexing...
    Z=Z.T                           # 
    for k in np.arange(N) :         # Count r.n. with toward sampling method
        i=0
        while(Y[k] >= C[i]) :
            i+=1
        Z[i][1]+=1
    print(Z)
