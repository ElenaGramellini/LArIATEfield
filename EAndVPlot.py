###############################
###      Important notes    ###
### the v is in mm/microsec ###
### the E is in V/cm       ###
###############################

import argparse
import math


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
    print type(v)
    return v


def muE2v(E, T):
    E = E/1000.
    v = (P1*(T-T0) + 1)*(P3*E*math.log(1 + P4/E) + P5*math.pow(E, P6)) + P2*(T-T0)
    print type(v)
    return v*10/E



import matplotlib.pyplot as plt
import numpy as np

fig1 = plt.figure(facecolor='white')
t1 = np.arange(460., 480.0, 0.1)
f2 = np.vectorize(E2v)
#line1 = plt.plot(t1, f2(t1,87.0),label="T = 87.0 K",linewidth=2.0)
#line2 = plt.plot(t1, f2(t1,88.4),label="T = 88.4 K",linewidth=2.0)
line3 = plt.plot(t1, f2(t1,90.3),label="T = 90.3 K",linewidth=2.0)
#line4 = plt.plot(t1, f2(t1,93.0),label="T = 93.0 K",linewidth=2.0)
plt.legend(bbox_to_anchor=(0.8, 0.5),
           bbox_transform=plt.gcf().transFigure)

plt.grid(True)
plt.title('Drift time dependence on E field from Walkowiak')
plt.xlabel('E field [V/cm]')
plt.ylabel('Drift Velocity [mm/$\mu$s]')
plt.show()



fig2 = plt.figure(facecolor='white')
t2 = np.arange(400., 1000.0, 0.1)
f3 = np.vectorize(muE2v)

line1 = plt.plot(t2, f3(t1,87.0),label="T = 87.0 K",linewidth=2.0)
line2 = plt.plot(t2, f3(t1,88.4),label="T = 88.4 K",linewidth=2.0)
line3 = plt.plot(t2, f3(t1,90.3),label="T = 90.3 K",linewidth=2.0)
line4 = plt.plot(t2, f3(t1,93.0),label="T = 93.0 K",linewidth=2.0)
plt.legend(bbox_to_anchor=(0.8, 0.5),
           bbox_transform=plt.gcf().transFigure)


plt.grid(True)
plt.title('Drift time dependence on E field from Walkowiak')
plt.xlabel('E field [V/cm]')
plt.ylabel('Mobility [cm^2/$\mu$s]')
plt.show()


#plt.plot(t1, E2v(t1,87), 'bo')


