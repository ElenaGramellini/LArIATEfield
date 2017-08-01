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


# This code takes as an argument the file
# we need to generate metadata for
parser = argparse.ArgumentParser()
parser.add_argument("V1"        , nargs='?', default = 0.  , type = float, help="insert voltage in V"   )
parser.add_argument("V2"        , nargs='?', default = 87. , type = float, help="insert voltage in V"   )
parser.add_argument("Temp"      , nargs='?', default = 90.7, type = float, help="insert argon temp in K")
parser.add_argument("Dx"        , nargs='?', default = 0.4 , type = float, help="insert spacing in cm"  )


args = parser.parse_args()
V1     = args.V1
V2     = args.V2
Temp   = args.Temp
Dx     = args.Dx


Efield = float(math.fabs(V1-V2))/float(Dx)
driftV = E2v(Efield,Temp)
driftT = float(Dx*10.)/float(driftV)


print "E field    = ", Efield, " V/cm;" 
print "Drift v    = ", driftV," mm/microsec;" 
print "Drift time = ", driftT," microsec"
