#!python3

import numpy as np

##----------------------------------
#  Methode des trapezes : 
def quadTrap(a,b,p,f):
    h = (b-a)/p
    res = 0.0
    x = a
    fx = f(x)
    while(x < b-1e-8):
        x += h
        fxPh = f(x)       
        res += fx + fxPh          
        fx = fxPh
        
    return res * h * 0.5    
##----------------------------------


##----------------------------------
#  Methode des pt milieu : 
def quadHerm(a,b,p,f,df):
    h = (b-a)/p
    h_div_2 = h * 0.5
    res = 0.0
    x = a
    eps = 1e-5
    while(x < b-1e-8):
        fx = f(x + h_div_2)
        res += fx
                
        x = x + h
    
    dfa = df(a) 
    dfb = df(b) 
    
    res += h * (dfb - dfa)/24
    
    return res * h
##----------------------------------


##----------------------------------
#  Methode des Gauss : 
def quadGauss(a,b,p,f):
    h = (b-a)/p
    res = 0.0
    x = a

    c1 = (-1. + np.sqrt(3)) / np.sqrt(12)  ### rajouté
    c2 = ( 1. + np.sqrt(3)) / np.sqrt(12)  ### rajouté
    
    hc1 = h * c1
    hc2 = h * c2

    while(x < b-1e-8):
        fx1 = f(hc1 + x)         
        fx2 = f(hc2 + x)         
        res += fx1 + fx2    
        
        x = x + h
        
    return res * h * 0.5
##----------------------------------

