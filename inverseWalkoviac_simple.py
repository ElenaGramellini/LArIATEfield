###############################
###      Important notes    ###
### the v is in mm/microsec ###
### the E is in V/cm       ###
###############################

import argparse
import math
#import scipy
from scipy.optimize import root


P1 = -0.01481 
P2 = -0.0075  
P3 =  0.141   
P4 = 12.4     
P5 =  1.627   
P6 =  0.317   
T0 = 90.371 

ErrP1 = 0.00095   
ErrP2 = 0.0028    
ErrP3 = 0.023     
ErrP4 = 2.7       
ErrP5 = 0.078     
ErrP6 = 0.021     


def E2v(E, T):
    E = E/1000.
    v = (P1*(T-T0) + 1)*(P3*E*math.log(1 + P4/E) + P5*math.pow(E, P6)) + P2*(T-T0)
    return v


def v2E(vel, T):
    e = 0
    for E in np.arange(300., 700.0, 0.1):
        vi = E2v(E,T)
        #print vi
        if vi > vel:
            e = E
            break
    return e

import matplotlib.pyplot as plt
import numpy as np

fig1 = plt.figure(facecolor='white')
t1 = np.arange(1.4, 1.6, 0.01)
f2 = np.vectorize(v2E)
line2 = plt.plot(t1, f2(t1,89.3),label="T = 89.3 K",linewidth=2.0)
line3 = plt.plot(t1, f2(t1,90.3),label="T = 90.3 K",linewidth=2.0)
line4 = plt.plot(t1, f2(t1,91.3),label="T = 91.3 K",linewidth=2.0)
plt.legend(bbox_to_anchor=(0.8, 0.5),
           bbox_transform=plt.gcf().transFigure)
plt.grid(True)
plt.title('E field dependence on drift velocity from (inverse) Walkowiak')
plt.ylabel('E field [V/cm]')
plt.xlabel('Drift Velocity [mm/$\mu$s]')
plt.show()


'''
t1 = np.arange(450., 500.0, 0.1)
f2 = np.vectorize(E2v)
line2 = plt.plot(t1, f2(t1,89.3),label="T = 89.3 K",linewidth=2.0)
line3 = plt.plot(t1, f2(t1,90.3),label="T = 90.3 K",linewidth=2.0)
line4 = plt.plot(t1, f2(t1,91.3),label="T = 91.3 K",linewidth=2.0)
plt.legend(bbox_to_anchor=(0.8, 0.5),
           bbox_transform=plt.gcf().transFigure)
plt.grid(True)
plt.title('Drift time dependence on E field from Walkowiak')
plt.xlabel('E field [V/cm]')
plt.ylabel('Drift Velocity [mm/$\mu$s]')
plt.show()
'''


#plt.plot(t1, E2v(t1,87), 'bo')

