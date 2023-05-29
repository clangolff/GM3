#!/usr/bin/python3
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import affichage


import algo
import data


"""
    Quadrature et équation des ondes 
"""

##----------------------------------
# But du programme :
# 1. Test quadrature simple.
# 2. Analyse de convergence.
# 3. Résolution de l'équation d'Helmholtz.
butPrgm = 1
print("Que souhaitez vous faire ?")
print(" 1. Test quadrature simple.")
print(" 2. Analyse de convergence.")
print(" 3. Resolution Helmholtz.")
butPrgm = input("Entrer le choix : ")

print("")

# Choix de la methode de quadrature  :
print("Choix de la méthode de quadrature ?")
print(" 1. Trapèze.")
print(" 2. Gauss.")
print(" 3. Hermite.")
choixQuad = input("Entrer le choix : ")
print("")

##----------------------------------



##----------------------------------
# I. Test Interpolation d'une fonction f :
if (butPrgm=="1"):
    # Intervalle d'intégration
    # Modifier ICI :
    a=0.0
    b=0.75
    
    # p-sous intervalles pour la formule de quadrature (composite) :
    # Modifier ICI :
    p = 3
    
    resQuad = 0.0
    if (choixQuad == "1"):
        resQuad = algo.quadTrap(a,b,p,data.f)
    if (choixQuad == "2"):
        resQuad = algo.quadGauss(a,b,p,data.f)
    if (choixQuad == "3"):
        resQuad = algo.quadHerm(a,b,p,data.f,data.df)
         
    print("Calcul integrale de f : ",resQuad)  
     
    # Illustration formule de quadrature :
    if(p <= 20):
        affichage.afficherQuad(a,b,p,data.f,choixQuad)   
    else:
        print("Trop d'intervalle pour être représenté.")
##----------------------------------

##----------------------------------
# II. Analyse de convergence :
if (butPrgm=="2"):
    
    # Intervalle d'intégration
    # Modifier ICI :
    a=0.0
    b=0.75
    
    # parametre d'oscillation kk
    # Modifier ICI :
    kk = 2.0
    
    ## Integral exacte (pour f(x) = cos(2k pi x), attention penser a modifier dans data !)
    valEx = 1/(2*kk*np.pi) * np.sin(1.5 * kk * np.pi)
    # Completer ICI (integrale pour f(x)=x²:
    #valEx = 0.75**3 / 3
    
    # p-sous intervalle pour la formule de quadrature :
    list_p = [4,8,16,32,64,128]
    
    list_err = []
    list_res = []
    for p in list_p:
    
        resQuad = 0.0
        if (choixQuad == "1"):
            resQuad = algo.quadTrap(a,b,p,data.f)
        if (choixQuad == "2"):
            resQuad = algo.quadGauss(a,b,p,data.f)
        if (choixQuad == "3"):
            resQuad = algo.quadHerm(a,b,p,data.f,data.df) 
            
        list_res.append(resQuad)    
        list_err.append(np.abs(resQuad-valEx))
    
        
    ## Tracer courbe erreur :
    poly = np.polyfit(np.log10(list_p),np.log10(list_err),1)
    print("")
    print("Droite approchée : y=",poly[0],"x - ",np.abs(poly[1]))
    print(list_err)
    
    affichage.afficherConv([np.log10(list_p)],[np.log10(list_err)])
##----------------------------------



##----------------------------------
# III. Resolution Helmholtz :
if (butPrgm=="3"):
    
    # Point (x,y) où on évalue la fonction u
    dx = 0.01
    dy = 0.01
    listX = np.arange(dx,5+dx*0.5,dx)
    listY = np.arange(-2.5,2.5+dy*0.5,dy)
    
    # Frequence ww et attenuation eps
    # Modifier ICI:
    ww = 10.0
    eps = 1.0j
    y0 = 0.0;
    
    p = 100

    div_2pi =  0.5/np.pi
    const = ww**2+eps
    res = np.zeros((len(listX),len(listY)),dtype=complex)
    for ix,x in enumerate(listX):
        resy = []
        # Completer ICI  
        myf = lambda xi : np.exp(1.0j*(listX[ix]*np.sqrt(const-xi**2)+xi*(listY-y0) ))
        mydf = lambda xi : myf(xi)*(-listX[ix]*xi/(const-xi**2)-(listY-y0))



        # Modifier ICI :
        a = -30.0
        b = 30.0
        resQuad = 0.0
        if (choixQuad == "1"):
            resQuad = algo.quadTrap(a,b,p,myf)
        if (choixQuad == "2"):
            resQuad = algo.quadGauss(a,b,p,myf)
        if (choixQuad == "3"):
            resQuad = algo.quadHerm(a,b,p,myf,mydf) 
            
        res[ix,:] = resQuad
        
    res = div_2pi * np.array(res)
    res = res.T
    
    # Affichage de la solution :
    affichage.afficherSol2D(listX,listY,res)
    #affichage.afficherSol3D(listX,listY,res)
##----------------------------------    


print("FIN \n")
########################################
