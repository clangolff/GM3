#!/usr/bin/python3
#-*- coding: utf-8 -*-

import numpy as np
import affichage

import algo
import data


"""
    Interpolation et dessin 
"""

## Attention : Pour executer le programme, il faut utiliser python3 main.py

##----------------------------------
# But du programme :
# 1. Test interpolation fonction 1D.
# 2. Visualiser des donnees.
# 3. Dessin relier des points.
butPrgm = 1
print("Que souhaitez vous faire ?")
print(" 1. Interpolation d'une fonction f.")
print(" 2. Visualiser les donnees.")
print(" 3. Dessin relier les points.")
butPrgm = input("Entrer le choix : ")

print("")
##----------------------------------

##----------------------------------
nomData = ""
if (butPrgm == "2" or butPrgm == "3"):
    # Choix des donnees :
    # 1. Dessin simple
    # 2. Cercle
    # 3. Dessin de Moustik
    choixData = 1
    print("Choix donnees ?")
    print(" 1. Trajectoire simple")
    print(" 2. Cercle.")
    print(" 3. Trajectoire de Moustik.")
    choixData = input("Entrer le choix : ")
    if (choixData =="1"):
        nomData = "dessin3.data"
    if (choixData =="2"):
        nomData = "dessin2.data"
    if (choixData =="3"):
        nomData = "dessin.data"
    
    print("")
##----------------------------------


##----------------------------------
# Test Interpolation d'une fonction f :
if (butPrgm=="1"):
    print("Choix type de points ?")
    print(" 1. Points équirépartis.")
    print(" 2. Points Chebychev.")
    typePt = input("Entrer le choix : ")
    print("")
    
    # Interpolation de la fonction f dans l'intervalle [a,b]
    a= -1.0
    b=  1.0
    
    # (N+1) points :
    N = 14
    h = 2.0 / N
    
    ptsInterpRef = []
    if (typePt == "1"):
        ptsInterpRef = np.linspace(-1.,1.,N+1)
    if (typePt == "2"):
        ptsInterpRef = np.cos( ( np.arange(0.0,N+1.0)*2.0 + 1.0 )*np.pi / (2.0*N+2.0) )  
    
    ptsInterpRef.sort()     
    ptsInterp = ( (np.array(ptsInterpRef)+1.0)*0.5 )*(b-a) + a
    valPtsInterp = data.f(ptsInterp)
    
    
    # Evaluation polynome interpolation :   
    a = ptsInterp[0]
    b = ptsInterp[-1]
    # K est le nombre de point à évaluer
    K = 50
    xx = np.linspace(a,b,K)
    yy = xx*0.0

    
    print("Choix méthode évaluation ?")
    print(" 1. Neville-Aitken.")
    print(" 2. Differences Divisées + Horner.")
    print(" 3. Hermite : Differences Divisées + Horner ordre 1.")
    print(" 4. Hermite : Differences Divisées + Horner ordre 2.")
    print(" 5. Hermite : Neville-Aitkens ordre 1.")
    print(" 6. Hermite : Neville-Aitkens ordre 2.")
    metho = input("Entrer le choix : ")
    print("")
    
    if(metho=="1"):
        yy = algo.NevilleAitken(xx,ptsInterp,valPtsInterp)
    if(metho=="2"):
        DD = algo.DiffDiv(ptsInterp,valPtsInterp)
        yy = algo.Horner(DD,ptsInterp,xx)
        
    if(metho=="3" or metho=="5"):
        ptsInterpHermite = []
        # On dedouble les points
        for e in ptsInterp:
            # Completer ICI :
            ptsInterpHermite.append(e)
            ptsInterpHermite.append(e)
        
        ptsInterpHermite = np.array(ptsInterpHermite)
        
        ValPtsInterp = data.f(ptsInterpHermite)
        # Completer ICI :
        ValDerivPtsInterp = data.df(ptsInterpHermite)
        
        if(metho=="3"):
            DD = algo.DiffDivHerm(ptsInterpHermite,ValPtsInterp,ValDerivPtsInterp)
            yy = algo.Horner(DD,ptsInterpHermite,xx)
        else:
            yy = algo.NevilleAitkenHerm(xx,ptsInterp,valPtsInterp,ValDerivPtsInterp)
    
    if(metho=="4" or metho=="6"):
        ptsInterpHermite = []
        # On detriple les points
        for e in ptsInterp:
            # Completer ICI :
            ptsInterpHermite.append(e)
            ptsInterpHermite.append(e)
            ptsInterpHermite.append(e)
        
        ptsInterpHermite = np.array(ptsInterpHermite)
        
        ValPtsInterp = data.f(ptsInterpHermite)
        # Completer ICI :
        ValDerivPtsInterp = data.df(ptsInterpHermite)
        ValDeriv2PtsInterp = data.d2f(ptsInterpHermite)
	
        if(metho=="4"):
            DD = algo.DiffDivHerm2(ptsInterpHermite,ValPtsInterp,ValDerivPtsInterp,ValDeriv2PtsInterp)
            yy = algo.Horner(DD,ptsInterpHermite,xx)
        else:
            yy = algo.NevilleAitkenHerm2(xx,ptsInterp,valPtsInterp,ValDerivPtsInterp,ValDeriv2PtsInterp)


    # Affichage Xt, Yt versus tt
    affichage.afficher1D([xx,ptsInterp],[yy,valPtsInterp])
##----------------------------------


##----------------------------------
# Visualiser donnees dessin :
if (butPrgm=="2"):
    # Donnees liste coordonnées :
    listPt = np.genfromtxt(nomData, delimiter="\t")
    
    XX = [e[0] for e in listPt]
    YY = [e[1] for e in listPt]
    
    # Affichage resultat :
    affichage.afficher1D([[],XX,[]],[[],YY,[]])
##----------------------------------


##----------------------------------
# Test dessin :
if (butPrgm=="3"):
    print("Choix type de points ?")
    print(" 1. Points équirépartis.")
    print(" 2. Points Chebychev.")
    typePt = input("Entrer le choix : ")
    print("")
    
    # Interpolation de la fonction f dans l'intervalle [a,b]
    a=-1.0
    b=1.0
    
    # Donnees liste coordonnées :
    listPt = np.genfromtxt(nomData, delimiter="\t")
    
    XX = [e[0] for e in listPt]
    YY = [e[1] for e in listPt]
    
    # (N+1) points :
    N = len(XX)-1
    h = 2.0 / N
    
    ptsInterpRef = []
    if (typePt == "1"):
        ptsInterpRef = np.arange(-1.0,1.0+0.9*h,h)
    if (typePt == "2"):
        ptsInterpRef = np.cos( ( np.arange(0.0,N+1.0)*2.0 + 1.0 )*np.pi / (2.0*N+2.0) )  
    
    ptsInterpRef.sort()     
    ptsInterp = ( (np.array(ptsInterpRef)+1.0)*0.5 )*(b-a) + a
    
    
    
    # Evaluation polynome interpolation :   
    a = ptsInterp[0]
    b = ptsInterp[-1]
    tt = np.arange(a,b+0.005*h,0.005*h)
    
    print("Choix méthode évaluation ?")
    print(" 1. Neville-Aitken.")
    print(" 2. Differences Divisées + Horner.")
    print(" 3. Hermite : Differences Divisees + Horner.")
    metho = input("Entrer le choix : ")
    print("")
    
    Xt = tt*0
    Yt = tt*0
    if(metho=="1"):
        Xt = algo.NevilleAitken(tt,ptsInterp,XX)
        Yt = algo.NevilleAitken(tt,ptsInterp,YY)
    if(metho=="2"):
        DD = algo.DiffDiv(ptsInterp,XX)
        Xt = algo.Horner(DD,ptsInterp,tt)
        DD = algo.DiffDiv(ptsInterp,YY)
        Yt = algo.Horner(DD,ptsInterp,tt)
        
    if(metho=="3"):
        ptsInterpHermite = []
        # On dedouble les points
        for e in ptsInterp:
            # Completer ICI :
            ptsInterpHermite.append(e)
            ptsInterpHermite.append(e)
            
        ptsInterpHermite = np.array(ptsInterpHermite)
        
        # On dedouble les valeurs XX :
        ValPtsInterpXX = []
        for e in XX:
            ValPtsInterpXX.append(e)
            ValPtsInterpXX.append(e)
        
        # On dedouble les valeurs YY :    
        ValPtsInterpYY = []
        for e in YY:
            ValPtsInterpYY.append(e)
            ValPtsInterpYY.append(e)
              
        ValPtsInterpXX = np.array(ValPtsInterpXX)
        ValPtsInterpYY = np.array(ValPtsInterpYY)
        
        # Calcul des derivees x'(ti)
        ValDerivPtsInterpXX = []
        for j,t in enumerate(ptsInterp):
            res = 0.0
            if (j >= 1 and j<= len(ptsInterp)-2):
                # Completer ICI :
                # X previous, t previous
                Xj_p = XX[j-1]
                tj_p = ptsInterp[j-1]
                # X , t
                tj = ptsInterp[j]
                Xj = XX[j] 
                # X next, t next
                Xj_n = XX[j+1]
                tj_n = ptsInterp[j+1]

                res = Xj_p*(t-tj_n)/((t-tj_p)*(tj_n-tj_p))+Xj_n*(t-tj_p)/((tj_n-t)*(tj_n-tj_p))+Xj*(tj_n+tj_n-2*t)/((tj_n-t)*(t-tj_p)) 
            
            if (j==0):
                # Completer ICI :
                res = (XX[j+1] - XX[j]) / (ptsInterp[j+1] - t)
            if (j==len(ptsInterp)-1):
                # Completer ICI :
                res = (XX[j] - XX[j-1]) / (t-ptsInterp[j-1])
            
            ValDerivPtsInterpXX.append(res)
        
        # On dedouble les valeurs x'(ti)    
        ValDerivPtsInterpXXBis = []    
        for e in ValDerivPtsInterpXX:
            ValDerivPtsInterpXXBis.append(e)
            ValDerivPtsInterpXXBis.append(e)
        
        # Calcul des derivees y'(ti)    
        ValDerivPtsInterpYY = []
        for j,t in enumerate(ptsInterp):
            if (j >= 1 and j<= len(ptsInterp)-2):
                # Completer ICI :
                # Y previous, t previous
                Yj_p = YY[j-1]
                tj_p = ptsInterp[j-1]
                # Y , t
                Yj = YY[j]
                tj = ptsInterp[j]
                # Y next , t next
                Yj_n = YY[j+1]
                tj_n = ptsInterp[j+1]
                
                res = Yj_p*(t-tj_n)/((t-tj_p)*(tj_n-tj_p))+Yj_n*(t-tj_p)/((tj_n-t)*(tj_n-tj_p))+Yj*(tj_n+tj_n-2*t)/((tj_n-t)*(t-tj_p)) 
            

            if (j==0):
                # Completer ICI :
                res = (YY[j+1] - YY[j]) / (ptsInterp[j+1] - t)
            if (j==len(ptsInterp)-1):
                # Completer ICI :
                res = (YY[j] - YY[j-1]) / (t-ptsInterp[j-1])
            
            ValDerivPtsInterpYY.append(res)
        
        # On dedouble les valeurs y'(ti)    
        ValDerivPtsInterpYYBis = []    
        for e in ValDerivPtsInterpYY:
            ValDerivPtsInterpYYBis.append(e)
            ValDerivPtsInterpYYBis.append(e)    
            
        ValDerivPtsInterpXXBis = np.array(ValDerivPtsInterpXXBis)
        ValDerivPtsInterpYYBis = np.array(ValDerivPtsInterpYYBis)
        
        DD = algo.DiffDivHerm(ptsInterpHermite,ValPtsInterpXX,ValDerivPtsInterpXXBis)
        Xt = algo.Horner(DD,ptsInterpHermite,tt)
        
        DD = algo.DiffDivHerm(ptsInterpHermite,ValPtsInterpYY,ValDerivPtsInterpYYBis)
        Yt = algo.Horner(DD,ptsInterpHermite,tt)
        
    # Affichage resultat plan :
    affichage.afficher1D([Xt,XX],[Yt,YY])
    
    # Affichage Xt, Yt versus tt
    affichage.afficher1Dbis([tt,tt,ptsInterp,ptsInterp],[Xt,Yt,XX,YY])   
##----------------------------------


print("FIN \n")
########################################
