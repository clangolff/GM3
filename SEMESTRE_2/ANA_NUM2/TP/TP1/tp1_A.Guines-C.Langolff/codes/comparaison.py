#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt

import algo
import data

# (N+1) points :
N = 15


# Interpolation de la fonction f dans l'intervalle [a,b]
a = -1.0
b =  1.0

ptsEquiref = []
ptsChebyref = []

#points equirépartie

ptsEquiref = np.linspace(-1.,1.,N+1)
#points de Tchbychev
ptsChebyref = np.cos((np.arange(0.0,N+1.0)*2.0 + 1.0 )*np.pi / (2.0*N+2.0))
#ptsChebyref = np.array(ptsChebyref)

ptsEquiref.sort()
ptsChebyref.sort()

ptsEqui =  0.5 * (ptsEquiref  + 1.) * (b - a) + a
ptsCheby = 0.5 * (ptsChebyref + 1.) * (b - a) + a

#valeur des point
valPtsEqui = data.f(ptsEqui)
valPtsCheby = data.f(ptsCheby)


# Evaluation polynome interpolation :
aEqui  = ptsEqui[0]
aCheby = ptsCheby[0]

bEqui  = ptsEqui[-1]
bCheby = ptsCheby[-1]

# K est le nombre de point à évaluer
K = 100

#vecteur de point d'évaluation
ptsEvalEqui  = np.linspace(aEqui,bEqui,K)
ptsEvalCheby = np.linspace(aCheby,bCheby,K)


# NA Neville Aitken
# H  DD + Horner
# HH DD + Horner + Hermite
# NH Neville Aitken + Hermite

yNAEqui  = ptsEvalEqui  * 0.
yHEqui   = ptsEvalEqui  * 0.
yHHEqui  = ptsEvalEqui  * 0.
yNHEqui  = ptsEvalEqui  * 0.



yNACheby  = ptsEvalCheby * 0.
yHCheby   = ptsEvalCheby * 0.
yHHCheby  = ptsEvalCheby * 0.
yNHCheby  = ptsEvalCheby * 0.



###############   ALGO   #########################



#Neville point equi
yNAEqui = algo.NevilleAitken(ptsEvalEqui,ptsEqui,valPtsEqui)


#neville point tcheby
yNACheby = algo.NevilleAitken(ptsEvalCheby,ptsCheby,valPtsCheby)

#horner equi
coeffBN = algo.DiffDiv(ptsEqui,valPtsEqui)
yHEqui = algo.Horner(coeffBN,ptsEqui,ptsEvalEqui)

#horner tcheby
coeffBN = algo.DiffDiv(ptsCheby,valPtsCheby)
yHCheby = algo.Horner(coeffBN,ptsCheby,ptsEvalCheby)


#horner hermite point equi
ptsInterpHermite = []
# On dedouble les points
for e in ptsEqui:
    # Completer ICI :
    ptsInterpHermite.append(e)
    ptsInterpHermite.append(e)

ptsInterpHermite = np.array(ptsInterpHermite)
ValPtsInterpHermite = data.f(ptsInterpHermite)
ValDerivPtsInterpHermite = data.df(ptsInterpHermite)
ValDerivPtsInterp = data.df(ptsEqui)

## j'ai échangé ValDerivPtsInterpHermite dans l'appel de la fonction
coeffBN = algo.DiffDivHerm(ptsInterpHermite,ValPtsInterpHermite,ValDerivPtsInterpHermite)
yHHEqui = algo.Horner(coeffBN,ptsInterpHermite,ptsEvalEqui)

#Neville hermite point equi
yNHEqui = algo.NevilleAitkenHerm(ptsEvalEqui,ptsInterpHermite,ValPtsInterpHermite,ValDerivPtsInterpHermite)

#horner hermite point tcheby
ptsInterpHermite = []
# On dedouble les points
for e in ptsCheby:
    # Completer ICI :
    ptsInterpHermite.append(e)
    ptsInterpHermite.append(e)

ptsInterpHermite = np.array(ptsInterpHermite)
ValPtsInterpHermite = data.f(ptsInterpHermite)
ValDerivPtsInterpHermite = data.df(ptsInterpHermite)
ValDerivPtsInterp = data.df(ptsCheby)

## j'ai échangé ValDerivPtsInterpHermite dans l'appel de la fonction
coeffBN = algo.DiffDivHerm(ptsInterpHermite,ValPtsInterpHermite,ValDerivPtsInterpHermite)
yHHCheby = algo.Horner(coeffBN,ptsInterpHermite,ptsEvalCheby)

#Neville hermite point tcheby
yNHCheby = algo.NevilleAitkenHerm(ptsEvalCheby,ptsInterpHermite,ValPtsInterpHermite,ValDerivPtsInterpHermite)


################# AFFICHAGE ######################



fig, axs = plt.subplots(4,2,figsize=(10,20))


#points Equi colonne 1
for i in range(4):
    axs[i,0].plot(ptsEqui,valPtsEqui,'k+',markersize=12)

#points cheby colonne 2
for i in range(4):
    axs[i,1].plot(ptsCheby,valPtsCheby,'r+',markersize=12)

# Neville Aitken
axs[0,0].plot(ptsEvalEqui,yNAEqui,'-',color='lawngreen',linewidth=1)
axs[0,0].set_title("points équi-répartis N = " + str(N))
axs[0,1].plot(ptsEvalCheby,yNACheby,'-',color='orange')
axs[0,1].set_title("points de Tchebychev N = " + str(N))
axs[0,0].set_ylabel("Neville Aitken")

# DD + horner
axs[1,0].plot(ptsEvalEqui,yHEqui,'-',color='lawngreen',linewidth=1)
axs[1,1].plot(ptsEvalCheby,yHCheby,'-',color='orange')
axs[1,0].set_ylabel("DD + Horner")

# DD + Horner + Hermite
axs[2,0].plot(ptsEvalEqui,yHHEqui,'-',color='lawngreen',linewidth=1)
axs[2,1].plot(ptsEvalCheby,yHHCheby,'-',color='orange')
axs[2,0].set_ylabel("DD + Horner + Hermite")

# NH Neville Aitken + Hermite
axs[3,0].plot(ptsEvalEqui,yNHEqui,'-',color='lawngreen',linewidth=1)
axs[3,1].plot(ptsEvalCheby,yNHCheby,'-',color='orange')
axs[3,0].set_ylabel("Neville Aitken + Hermite")

#plt.show()
plt.savefig("comparaisonABS15.pdf")
