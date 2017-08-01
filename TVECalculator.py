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
    E = float(E)/1000.
    v = (P1*(T-T0) + 1)*(P3*E*math.log(1 + P4/E) + P5*math.pow(E, P6)) + P2*(T-T0)
    return v


def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step

# This code takes as an argument the file
# we need to generate metadata for
parser = argparse.ArgumentParser()
parser.add_argument("T"         , nargs='?', default = 320. , type = float, help="insert voltage in V"   )
parser.add_argument("Temp"      , nargs='?', default = 90.7 , type = float, help="insert argon temp in K")
parser.add_argument("Dx"        , nargs='?', default = 47   , type = float, help="insert spacing in cm"  )


args = parser.parse_args()

T     = args.T
Temp   = args.Temp
Dx     = args.Dx

Efield = 0
driftT = T
driftV = float(Dx*10.)/float(T)

for Etemp in frange(200,1900,0.001):
    vtemp = E2v(Etemp,Temp)
#    print vtemp, Etemp
    if math.fabs(vtemp - driftV) < 0.001:
        Efield = Etemp
        break


print "E field    = ", Efield, " V/cm;" 
print "Drift v    = ", driftV," mm/microsec;" 
print "Drift time = ", driftT," microsec"
