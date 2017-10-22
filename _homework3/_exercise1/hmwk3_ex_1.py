import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random, seed
import time
seed=(1234)                        

def Distribution(n_item) :          # Generate a random discrete distribution of n_item
    r = random(size=(n_item))       #  elements 
                                    # i. Generation of n_item numbers
    Z = np.sum(r)                   # ii. Computation of normalization constant 
    p = r/Z                         # Normalization
    #print('sum over p = ',np.sum(p)) # Verification 
    return(p)
def ExponentialDistribution(n_item) :
    r = -np.log(np.random.uniform(size=n_item))
                                    # i. Generation of n_item numbers
    Z = np.sum(r)                   # ii. Computation of normalization constant 
    p = r/Z                         # Normalization
    return(p)

def UnDemiDistribution(n_item) :    
    r = 1/np.sqrt(np.random.uniform(size=n_item))
                                    # i. Generation of n_item numbers
    Z = np.sum(r)                   # ii. Computation of normalization constant 
    p = r/Z                         # Normalization
    return(p)

def AcceptRejectMethod(N,p,plot) :       # Generate random numbers w.r.t the distribution p
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
    mean = np.mean(np.abs(p-y))     # TO EVALUATE SAMPLING

    if plot==True :
        plt.plot(x,p,'o',label='dist')
        plt.plot(x,y,'o',label='r.n.')
        plt.legend()
        plt.show()
    return(mean)

def TowerSampling(N,p,plot) :       # Generate random numbers w.r.t the distribution p
    C = np.cumsum(p)*np.size(p)     # Creation of the cumulative
    #print('C_n =',C[-1])            # Verification 
    Y = random(size=(N))*np.size(p) # Generate N r.n. 
    x = np.arange(np.size(p))       # Just indexing...
    m=np.zeros(N)                   # Array which would be [4,0,1,0,5,2,0,1,(...),n_item,(...)]
    for i in np.arange((np.size(p))) :  # Test of TowerSampling
        m += np.ma.getmask(np.ma.masked_greater_equal(Y,C[i]))
    y=np.histogram(m,bins=np.size(p))[0]/N  # Returns an array which is [nb_0,nb_1,
                                            # (...),nb_n_item] normalized by nb of tirages
    mean = np.mean(np.abs(p-y))      # TO EVALUATE SAMPLING
    if plot==True :
        plt.plot(x,p,'o',label='dist')
        plt.plot(x,y,'o',label='r.n.')
        plt.legend()
        plt.show()
    return(mean)

#def main() :

