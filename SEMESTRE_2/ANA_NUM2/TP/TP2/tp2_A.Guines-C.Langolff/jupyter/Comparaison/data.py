#!/usr/bin/python3
#-*- coding: utf-8 -*-

import numpy as np
import copy
  

##----------------------------------
#  fonction f a integrer :
def f(x):
    # Parametre k :
    kk = 5.0
    ## Fonction cos :
    # Completer ICI :
    #res = np.cos(2 * kk * np.pi * x)	#res = ...
    
    # Autre fonction de votre choix :
    #res = x**2
    res = 1 / (1+25*x**2)
    return res
##---------------------------------- 


##----------------------------------
#  derivee df de la fonction f :
def df(x):
    # Parametre k :
    kk = 5.0
    # Fonction cos' :
    # Completer ICI :
    #res = - 2 * kk * np.pi * np.sin(2 * kk * np.pi * x)	#res = ...
    #res = 2 *x
    res = -50*x/(1+25*x**2)**2
    return res
##----------------------------------  


