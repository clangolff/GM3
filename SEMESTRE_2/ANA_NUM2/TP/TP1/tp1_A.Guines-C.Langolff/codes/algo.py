#!/usr/bin/python3
#-*- coding: utf-8 -*-

import numpy as np
import copy  



##----------------------------------
#  Algorithme de Neville-Aitken :
def NevilleAitken(ptsEval,PtsInterp,valPtsInterp) :
    nbPts = len(PtsInterp)
    nbPtsEval = len(ptsEval)

    #TabNA correspond à la colonne c du tableau de Neville
    TabNA = np.zeros((nbPts,nbPtsEval))
    #TabNANext correspond à la colonne c+1 du tableau de Neville
    TabNAnext = np.zeros((nbPts,nbPtsEval))

    # A l'initialisation, TabNA correspond à la colonne c=0
    for i in range(nbPtsEval) :
        TabNA[:,i] += valPtsInterp

    # Calcul des colonnes du tableaude Neville :
    for j in range(nbPts - 1) :
        # Calcul de la colonne c+1 du tableau :
        for i in range(nbPts - j -1) :
            pt1 = PtsInterp[i]
            pt2 = PtsInterp[i + j + 1]
            TabNAnext[i,:] = (TabNA[i,:] * (pt2 - ptsEval) - TabNA[i+1,:] * (pt1 - ptsEval)) / (pt2 - pt1)

        # Passage de c à c+1 :
        TabNA = TabNAnext * 1.0

    return TabNA[0,:]
##----------------------------------



##----------------------------------
#  Algorithme des Differences-Divisées :
def DiffDiv(ptsInterp,valPtsInterp) :
    nbPts = len(ptsInterp)
    # Liste coefficient base de Newton :
    coeffBN = np.zeros(nbPts)

    #TabDD correspond à la colonne c du tableau des DD
    TabDD = np.zeros(nbPts)
    #TabNANext correspond à la colonne c+1 du tableau de Neville
    TabDDnext = np.zeros(nbPts)

    # A l'initialisation, TabDD correspond à la colonne c=0
    TabDD = valPtsInterp

    #Premier coefficient base Newton :
    coeffBN[0] = TabDD[0]

    # Calcul des colonnes du tableaude DD :
    for j in range(nbPts-1) :
        # Calcul de la colonne c+1 du tableau :
        for i in range(nbPts-j-1) :
            # Completer ICI :
            pt1 = ptsInterp[i]
            pt2 = ptsInterp[i+j+1]
            TabDDnext[i] = (TabDD[i+1] - TabDD[i]) / (pt2-pt1)

        # Passage de c à c+1 :
        TabDD = TabDDnext * 1.
        # On recupère le coeffcient c+1 de la décomposition dans la base de Newton
        coeffBN[j+1] = TabDD[0]

    return coeffBN
##----------------------------------




##----------------------------------
#  Algorithme de Horner:
def Horner(coeffBN,ptsInterp,ptsEval) :
    nb = len(coeffBN)
    # Initialisation
    # Completer ICI :
    res = coeffBN[nb-2] + coeffBN[nb-1] * (ptsEval - ptsInterp[nb-2])

    # Iterations :
    # Completer ICI :
    for i in range(nb-3,-1,-1) :
        res = coeffBN[i] + (ptsEval - ptsInterp[i]) * res

    return res
##----------------------------------





#----------------------------------
#  Algorithme des Differences-Divisées hermite d'ordre 1 :
def DiffDivHerm(ptsInterp,valPtsInterp,valDerivPtsInterp):
    nbPts = len(ptsInterp)

    # Liste coefficient base de Newton :
    coeffBN = np.zeros(nbPts)

    #TabDD correspond à la colonne c du tableau des DD
    TabDD = np.zeros(nbPts)

    #TabDDNext correspond à la colonne c+1 du tableau des DD
    TabDDnext = np.zeros(nbPts)

    # A l'initialisation, TabDD correspond à la colonne c=0
    TabDD = valPtsInterp

    #Premier coefficient base Newton :
    coeffBN[0] = TabDD[0]

    # Calcul des colonnes du tableaude DD :
    for j in range(nbPts-1) :
        # Calcul de la colonne c+1 du tableau :
        for i in range(nbPts-j-1) :
            # Completer ICI :
            pt1 = ptsInterp[i]
            pt2 = ptsInterp[i+j+1]
            if (np.abs(pt2 - pt1) > 1e-8):
                TabDDnext[i] = (TabDD[i+1] - TabDD[i]) / (pt2-pt1)
            else :
                TabDDnext[i] = valDerivPtsInterp[i]
        # Passage de c à c+1 :
        TabDD = TabDDnext * 1.
        # On recupère le coeffcient c+1 de la décomposition dans la base de Newton :
        coeffBN[j+1] = TabDD[0]

    return coeffBN
##----------------------------------

#  Algorithme des Differences-Divisées hermite ordre 2:
def DiffDivHerm2(ptsInterp,valPtsInterp,valDerivPtsInterp,valDeriv2PtsInterp):
    nbPts = len(ptsInterp)

    # Liste coefficient base de Newton :
    coeffBN = np.zeros(nbPts)

    #TabDD correspond à la colonne c du tableau des DD
    TabDD = np.zeros(nbPts)

    #TabDDNext correspond à la colonne c+1 du tableau des DD
    TabDDnext = np.zeros(nbPts)

    # A l'initialisation, TabDD correspond à la colonne c=0
    TabDD = valPtsInterp

    #Premier coefficient base Newton :
    coeffBN[0] = TabDD[0]

    # Calcul des colonnes du tableaude DD :
    for j in range(nbPts-1) :
        # Calcul de la colonne c+1 du tableau :
        for i in range(nbPts-j-1) :
            # Completer ICI :
            pt1 = ptsInterp[i]
            pt2 = ptsInterp[i+j+1]
            
            if (np.abs(pt2 - pt1) > 1e-8):
                TabDDnext[i] = (TabDD[i+1] - TabDD[i]) / (pt2-pt1)
            else :
                if (j==0):
                    TabDDnext[i] = valDerivPtsInterp[i]
                else : 
                    TabDDnext[i] = valDeriv2PtsInterp[i] / 2

        # Passage de c à c+1 :
        TabDD = TabDDnext * 1.
        # On recupère le coeffcient c+1 de la décomposition dans la base de Newton :
        coeffBN[j+1] = TabDD[0]

    return coeffBN
##----------------------------------


#  Algorithme de Neville-Aitken pour interpolation d'Hermite ordre 1:
def NevilleAitkenHerm(PtsEval,PtsInterp,ValPtsInterp,ValDerivPtsInterp):
    nbPts = len(PtsInterp)

    #TabNA correspond à la colonne c du tableau de Neville
    TabNA = np.zeros((nbPts,len(PtsEval)))
    # A l'initialisation, TabNA correspond à la colonne c=0
    for i in range(len(PtsEval)):
        TabNA[:,i] = TabNA[:,i] + ValPtsInterp
    #TabNANext correspond à la colonne c+1 du tableau de Neville
    TabNANext = np.zeros((nbPts,len(PtsEval)))


    # Calcul des colonnes du tableaude Neville :
    for c in range(nbPts-1):
        # Calcul de la colonne c+1 du tableau :
        for l in range(nbPts-c-1):
            pt1 = PtsInterp[l]
            pt2 = PtsInterp[l+c+1]

            if (np.abs(pt2 -pt1) > 1e-8):
                TabNANext[l,:] = ( (pt2 - PtsEval)*TabNA[l,:] - (pt1 - PtsEval)*TabNA[l+1,:] ) / (pt2 - pt1)
            else:
                TabNANext[l,:] = TabNA[l,:] + ValDerivPtsInterp[l] * (PtsEval - pt1)

        # Passage de c à c+1 :
        TabNA = TabNANext*1.0

    return TabNA[0,:]
##----------------------------------


#  Algorithme de Neville-Aitken pour interpolation d'Hermite à l'ordre 2:
def NevilleAitkenHerm2(PtsEval,PtsInterp,ValPtsInterp,ValDerivPtsInterp,ValDeriv2PtsInterp):
    nbPts = len(PtsInterp)

    #TabNA correspond à la colonne c du tableau de Neville
    TabNA = np.zeros((nbPts,len(PtsEval)))
    # A l'initialisation, TabNA correspond à la colonne c=0
    for i in range(len(PtsEval)):
        TabNA[:,i] = TabNA[:,i] + ValPtsInterp
    #TabNANext correspond à la colonne c+1 du tableau de Neville
    TabNANext = np.zeros((nbPts,len(PtsEval)))


    # Calcul des colonnes du tableaude Neville :
    for c in range(nbPts-1):
        # Calcul de la colonne c+1 du tableau :
        for l in range(nbPts-c-1):
            pt1 = PtsInterp[l]
            pt2 = PtsInterp[l+c+1]

            if (np.abs(pt2 - pt1) > 1e-8):
                TabNANext[l,:] = ( (pt2 - PtsEval)*TabNA[l,:] - (pt1 - PtsEval)*TabNA[l+1,:] ) / (pt2 - pt1)
            else:
                if (c==0):
                    TabNANext[l,:] = TabNA[l,:] + ValDerivPtsInterp[l] * (PtsEval - pt1)
                else : 
                    TabNANext[l,:] = TabNA[l,:] + ValDeriv2PtsInterp[l] * ((PtsEval - pt1)**2) / 2

        # Passage de c à c+1 :
        TabNA = TabNANext*1.0

    return TabNA[0,:]
##----------------------------------
