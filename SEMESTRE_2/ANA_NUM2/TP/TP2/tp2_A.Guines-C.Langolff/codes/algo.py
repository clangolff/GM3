#!/usr/bin/python3
#-*- coding: utf-8 -*-

import numpy as np
import copy  
import data

##----------------------------------
#  Methode des trapezes : 
def quadTrap(a,b,p,f):
    h = (b-a)/p
    res = 0.0
    x = a
    fx = f(x)
    while(x < b-1e-8):
        # Completer ICI :
        x += h
        fxPh = f(x)        ### fxPh = ...
        res += fx + fxPh   ### res += ...
        
        fx = fxPh
        
    return res * h * 0.5     ### return res
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
        # Completer ICI :
        fx = f(x + h_div_2)	#fx = ...
        res += fx	#res += ... 
                
        x = x + h
    
    dfa = df(a) 
    dfb = df(b) 
    
    # Completer ICI :
    res += h * (dfb - dfa)/24	#res += ..;
    
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
        # Completer ICI :
        fx1 = f(hc1 + x)         ### changé fx1 = ...
        fx2 = f(hc2 + x)         ### changé ...
        res += fx1 + fx2        ### changé res += ...
        
        x = x + h
        
    return res * h * 0.5            ### changé return res
##----------------------------------

