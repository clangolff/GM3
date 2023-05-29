#!/usr/bin/python3
#-*- coding: utf-8 -*-

import numpy as np
import copy
  

##----------------------------------
#  fonction f a interpoler :
def f(Pts):
    res = []
    # Evaluation de f sur la liste des points Pts:
    for p in Pts:
        # Calcul de f(p) :
        ## Cosinus :
        #tmp = np.cos(2*np.pi*p)
        
        # f(p) = |p|
        tmp = np.abs(p)
        
        
        ## 1 / (1+25 x^2) :
        #tmp = 1.0 / (1+25*p*p)
        
        res.append(tmp)
        
    return np.array(res)
##---------------------------------- 


##----------------------------------
#  derivee df de la fonction f a interpoler :
def df(Pts):
    res = []
    eps = 1e-5
    
    # Evaluation de f sur la liste des points Pts:
    res = 0.5*(f(Pts+eps) - f(Pts-eps))/eps
    return np.array(res)
##----------------------------------    


##----------------------------------
#  derivee 2nd d2f de la fonction f a interpoler :
def d2f(Pts):
    res = []
    eps = 1e-5
    
    # Evaluation de f sur la liste des points Pts:
    res = (f(Pts+eps) - 2*f(Pts) + f(Pts-eps))/(eps*eps)
    return np.array(res)
##----------------------------------    
