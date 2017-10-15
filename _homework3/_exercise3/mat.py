import numpy as np
from numpy.random import random, seed
import matplotlib.pyplot as plt

seed(1234)

def in_circle(x, y):
    # function that returns true if a point (x, y) is inside the unit circle,
    # and false otherwise
    if x*x + y*y <= 1:
        return True
    else : return False

def in_square(x, y):
    if (abs(x) <= 1. and abs(y) <= 1.) :
        return True
    else: return False

def trajectory(nstep, step) :
    traj            = np.zeros((nstep, 2))  # define trajectory set
    step_x, step_y  = step, step            # define step size for x, y
    acceptance      = 0                     # initialize acceptance
    circlecompt     = 0                     # initialiaze the circle counter to 0
    for i in range(nstep-1) :
        # propose a move between :
        # x +/- dx, with dx a r.v. in [-step, step]
        x0, y0  = traj[i, 0], traj[i, 1]
        dx, dy  = (2*step_x*random()) - step_x, (2*step_y*random()) - step_y
        x, y    = x0 + dx , y0 + dy     # move
        if in_square(x, y) :
            # if the move is in the unit square, update the trajectory, increase
            # accceptance by one
            traj[i+1] = x, y
            acceptance += 1
            if in_circle : circlecompt += 1
        else :
            # else, stays here 
            traj[i+1] = x0, y0
    return traj, acceptance/float(nstep), circlecompt

### Question 1 :
step = 1.
N = [100, 1000, 4000, 20000]
T = [trajectory(N[i], step) for i in range(len(N))]

fig, ax = plt.subplots(2, 2)
plt.suptitle('Monte Carlo Markov Chain pi sampling for different trajectories of length n.')
ax[0, 0].plot(T[0][0][:,0], T[0][0][:,1])
ax[0, 0].set_title('n = ' + str(N[0]))
ax[0, 1].plot(T[1][0][:,0], T[1][0][:,1])
ax[0, 1].set_title('n = ' + str(N[1]))
ax[1, 0].plot(T[2][0][:,0], T[2][0][:,1])
ax[1, 0].set_title('n = ' + str(N[2]))
ax[1, 1].plot(T[3][0][:,0], T[3][0][:,1])
ax[1, 1].set_title('n = ' + str(N[3]))
plt.show()

### Question 2 :
S = np.linspace(0.1, 2., num = 100) # list of steps between 0.01 and 5.
nstep = 10**4
T = [trajectory(nstep, S[i]) for i in range(len(S))]

A = np.array([T[i][1] for i in range(len(S))]) # acceptance list

# print the best(s) empricial 1/2 step 
print 'The best empirical 1/2 step size is step = ' + str( S[np.argmin(abs(A - 0.5))])
plt.plot(S, A) ; plt.title('Acceptance ratio vs space step') ; plt.show()

### Question 3 :
