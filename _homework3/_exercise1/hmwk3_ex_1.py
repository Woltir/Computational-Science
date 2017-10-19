import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random, seed

seed=(1234)                        

def Distribution(n_item) :          # Generate a random discrete distribution of n_item
    r = random(size=(n_item))       #  elements 
                                    # i. Generation of n_item numbers
    Z = np.sum(r)                   # ii. Computation of normalization constant 
    print('Z=',Z)                   #
    p = r/Z                         # Normalization
    print('sum over p = ',np.sum(p)) # Verification 
    return(p)
    
def AcceptRejectMethod(N,p) :       # Generate random numbers w.r.t the distribution p
    X = random(size=(2,N))*np.size(p) ; I = X[0].astype(int) 
                                    # Generation of 2N r.n. (X,Y)
                                    # I is the int part of X in order to have a discrete r.n.
    Z = (X[1]<p[I]*np.size(p),I)    # Z is a bi-vector which includes [ResultOfTest,valueOfX]
    #print(I)                       # Show the r.n. to serif with eyes
    Z=Z[0]*1,Z[1]                   # Transform boolean in {0 or 1}
    x=np.arange(np.size(p))         # x=[0,1,2,(...),n_item]
    y=np.histogram(Z[1][np.nonzero(Z[0])],bins=np.size(p))[0]/np.sum(Z[0])
                                    # Returns an array which is [nb_0 success,nb_1 success,
                                    # (...),nb_n_item success] normalized by nb of success
    plt.plot(x,p,'o',label='dist')
    plt.plot(x,y,'o',label='r.n.')
    plt.legend()
    plt.show()
    
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
    x,y=Z.T
    plt.plot(x,p,'o',label='dist')
    plt.plot(x,y/N,'o',label='r.n.')
    plt.legend()
    plt.show()
    print(Z)
