#!/usr/bin/python3
#-*- coding: utf-8 -*-

import numpy as np


import algo
import data

nomData = "dessin4.data"

# Interpolation de la fonction f dans l'intervalle [a,b]
a=-1.0
b=1.0
    
# Donnees liste coordonnées :
listPt = np.genfromtxt(nomData, delimiter="\t")
    
ptsInterpX = [e[0] for e in listPt]
ptsInterpY = [e[1] for e in listPt]
    
# (N+1) points :
N = len(ptsInterpX)-1
h = 2.0 / N
    
ptsEquiref = []
ptsChebyref = []

#points equirépartie    
ptsEquiref = np.linspace(-1.,1.,N+1) 

#points de Tchbychev
ptsChebyref = np.cos((np.arange(0.0,N+1.0)*2.0 + 1.0 )*np.pi / (2.0*N+2.0))   


ptsEquiref.sort()
ptsChebyref.sort()
    
ptsEqui =  0.5 * (ptsEquiref  + 1.) * (b - a) + a
ptsCheby = 0.5 * (ptsChebyref + 1.) * (b - a) + a


# Evaluation polynome interpolation :   
a = ptsEqui[0]
b = ptsEqui[-1]
tt = np.arange(a,b+0.005*h,0.005*h)


# NA Neville Aitken 
# H  DD + Horner 
# HH DD + Horner + Hermite
# NH Neville Aitken + Hermite


# parametre X en focntion de t
XtEquiNA = tt*0
XtChebyNA = tt*0

XtEquiH = tt*0
XtChebyH = tt*0

XtEquiHH = tt*0
XtChebyHH = tt*0

XtEquiNH = tt*0
XtChebyNH = tt*0

# parametre y en fonction de t
YtEquiNA = tt*0
YtChebyNA = tt*0

YtEquiH = tt*0
YtChebyH = tt*0

YtEquiHH = tt*0
YtChebyHH = tt*0

YtEquiNH = tt*0
YtChebyNH = tt*0

#Neville point Equi
XtEquiNA = algo.NevilleAitken(tt,ptsEqui,ptsInterpX)
YtEquiNA = algo.NevilleAitken(tt,ptsEqui,ptsInterpY)

#Neville point de Cheby
XtChebyNA = algo.NevilleAitken(tt,ptsCheby,ptsInterpX)
YtChebyNA = algo.NevilleAitken(tt,ptsCheby,ptsInterpY)


#Horner point Equi
DD = algo.DiffDiv(ptsEqui,ptsInterpX)
XtEquiH = algo.Horner(DD,ptsEqui,tt)

DD = algo.DiffDiv(ptsEqui,ptsInterpY)
YtEquiH = algo.Horner(DD,ptsEqui,tt)

#Horner point Cheby
DD = algo.DiffDiv(ptsCheby,ptsInterpX)
XtChebyH = algo.Horner(DD,ptsCheby,tt)

DD = algo.DiffDiv(ptsCheby,ptsInterpY)
YtChebyH = algo.Horner(DD,ptsCheby,tt)




# Horner + Hermite pts Equi

ptsInterpHermite = []
# On dedouble les points
for e in ptsEqui:
    ptsInterpHermite.append(e)
    ptsInterpHermite.append(e)
    
ptsInterpHermite = np.array(ptsInterpHermite)



# On dedouble les valeurs ptsInterpX :
ValPtsInterpX = []
for e in ptsInterpX:
    ValPtsInterpX.append(e)
    ValPtsInterpX.append(e)

# On dedouble les valeurs ptsInterpY :    
ValPtsInterpY = []
for e in ptsInterpY:
    ValPtsInterpY.append(e)
    ValPtsInterpY.append(e)

ValPtsInterpX = np.array(ValPtsInterpX)
ValPtsInterpY = np.array(ValPtsInterpY)


# Calcul des derivees x'(ti)
ValDerivPtsInterpX = []
for j,t in enumerate(ptsEqui):
    res = 0.0
    if (j >= 1 and j<= len(ptsEqui)-2):
        # X previous
        Xj_p = ptsInterpX[j-1]
        # X 
        Xj = ptsInterpX[j]
        # X next
        Xj_n = ptsInterpX[j+1]
        
        # t previous
        tj_p = ptsEqui[j-1]
       
        # t next
        tj_n = ptsEqui[j+1]
        
        res = Xj_p*(t-tj_n)/((t-tj_p)*(tj_n-tj_p))+Xj_p*(t-tj_p)/((tj_n-t)*(tj_n-tj_p))+Xj*(tj_p+tj_n-2*t)/((tj_n-t)*(t-tj_p))
    if (j==0):
        res = (ptsInterpX[j+1] - ptsInterpX[j]) / (ptsEqui[j+1] - t)
    if (j==len(ptsEqui)-1):
        res = (ptsInterpX[j] - ptsInterpX[j-1]) / (t - ptsEqui[j-1])
            
    ValDerivPtsInterpX.append(res)
        
# On dedouble les valeurs x'(ti)    
ValDerivPtsInterp2X = []    
for e in ValDerivPtsInterpX:
    ValDerivPtsInterp2X.append(e)
    ValDerivPtsInterp2X.append(e)
        
# Calcul des derivees y'(ti)    
ValDerivPtsInterpY = []
for j,t in enumerate(ptsEqui):
    res = 0.0
    
    if (j >= 1 and j<= len(ptsEqui)-2):
        # Y previous
        Yj_p = ptsInterpY[j-1]
        # Y 
        Yj = ptsInterpY[j]
        # Y next
        Yj_n = ptsInterpY[j+1]
        
        # t previous
        tj_p = ptsEqui[j-1]
        
        # t next
        tj_n = ptsEqui[j+1]
        
        res = Yj_p*(t-tj_n)/((t-tj_p)*(tj_n-tj_p))+Yj_p*(t-tj_p)/((tj_n-t)*(tj_n-tj_p))+Yj*(tj_p+tj_n-2*t)/((tj_n-t)*(t-tj_p))
    if (j==0):
        res = (ptsInterpY[j+1] - ptsInterpY[j]) / (ptsEqui[j+1] - t)
    if (j==len(ptsEqui)-1):
        res = (ptsInterpY[j] - ptsInterpY[j-1]) / (t - ptsEqui[j-1])
            
    ValDerivPtsInterpY.append(res)
        
# On dedouble les valeurs y'(ti)    
ValDerivPtsInterp2Y = []    
for e in ValDerivPtsInterpY:
    ValDerivPtsInterp2Y.append(e)
    ValDerivPtsInterp2Y.append(e)    
            
               
               
ValDerivPtsInterp2X = np.array(ValDerivPtsInterp2X)
ValDerivPtsInterp2Y = np.array(ValDerivPtsInterp2Y)
            
               
               
DD = algo.DiffDivHerm(ptsInterpHermite,ValPtsInterpX,ValDerivPtsInterp2X)
XtEquiHH = algo.Horner(DD,ptsInterpHermite,tt)
        
DD = algo.DiffDivHerm(ptsInterpHermite,ValPtsInterpY,ValDerivPtsInterp2Y)
YtEquiHH = algo.Horner(DD,ptsInterpHermite,tt)

               
               
               
# Horner + Hermite pts Cheby

ptsInterpHermite = []
# On dedouble les points
for e in ptsCheby:
    ptsInterpHermite.append(e)
    ptsInterpHermite.append(e)
    
ptsInterpHermite = np.array(ptsInterpHermite)



# On dedouble les valeurs ptsInterpX :
ValPtsInterpX = []
for e in ptsInterpX:
    ValPtsInterpX.append(e)
    ValPtsInterpX.append(e)

# On dedouble les valeurs ptsInterpY :    
ValPtsInterpY = []
for e in ptsInterpY:
    ValPtsInterpY.append(e)
    ValPtsInterpY.append(e)

ValPtsInterpX = np.array(ValPtsInterpX)
ValPtsInterpY = np.array(ValPtsInterpY)


# Calcul des derivees x'(ti)
ValDerivPtsInterpX = []
for j,t in enumerate(ptsCheby):
    res = 0.0
    
    if (j >= 1 and j<= len(ptsCheby)-2):
        # X previous
        Xj_p = ptsInterpX[j-1]
        # X 
        Xj = ptsInterpX[j]
        # X next
        Xj_n = ptsInterpX[j+1]
        
        # t previous
        tj_p = ptsCheby[j-1]
    
        # t next
        tj_n = ptsCheby[j+1]
        res = Xj_p*(t-tj_n)/((t-tj_p)*(tj_n-tj_p))+Xj_p*(t-tj_p)/((tj_n-t)*(tj_n-tj_p))+Xj*(tj_p+tj_n-2*t)/((tj_n-t)*(t-tj_p))
    if (j==0):
        res = (ptsInterpX[j+1] - ptsInterpX[j]) / (ptsCheby[j+1] - t)
    if (j==len(ptsCheby)-1):
        res = (ptsInterpX[j] - ptsInterpX[j-1]) / (t - ptsCheby[j-1])
            
    ValDerivPtsInterpX.append(res)
        
# On dedouble les valeurs x'(ti)    
ValDerivPtsInterp2X = []    
for e in ValDerivPtsInterpX:
    ValDerivPtsInterp2X.append(e)
    ValDerivPtsInterp2X.append(e)
        
# Calcul des derivees y'(ti)    
ValDerivPtsInterpY = []
for j,t in enumerate(ptsCheby):
    res = 0.0
    
    if (j >= 1 and j<= len(ptsCheby)-2):
        # Y previous
        Yj_p = ptsInterpY[j-1]
        # Y 
        Yj = ptsInterpY[j]
        # Y next
        Yj_n = ptsInterpY[j+1]
        
        # t previous
        tj_p = ptsCheby[j-1]
        
        # t next
        tj_n = ptsCheby[j+1]
    
        res = Xj_p*(t-tj_n)/((t-tj_p)*(tj_n-tj_p))+Xj_p*(t-tj_p)/((tj_n-t)*(tj_n-tj_p))+Xj*(tj_p+tj_n-2*t)/((tj_n-t)*(t-tj_p))
    
    if (j==0):
        res = (ptsInterpY[j+1] - ptsInterpY[j]) / (ptsCheby[j+1] - t)
    if (j==len(ptsCheby)-1):
        res = (ptsInterpY[j] - ptsInterpY[j-1]) / (t - ptsCheby[j-1])
    
    ValDerivPtsInterpY.append(res)
        
# On dedouble les valeurs y'(ti)    
ValDerivPtsInterp2Y = []    
for e in ValDerivPtsInterpY:
    ValDerivPtsInterp2Y.append(e)
    ValDerivPtsInterp2Y.append(e)    
            
               
               
ValDerivPtsInterp2X = np.array(ValDerivPtsInterp2X)
ValDerivPtsInterp2Y = np.array(ValDerivPtsInterp2Y)
            
               
               
DD = algo.DiffDivHerm(ptsInterpHermite,ValPtsInterpX,ValDerivPtsInterp2X)
XtChebyHH = algo.Horner(DD,ptsInterpHermite,tt)
        
DD = algo.DiffDivHerm(ptsInterpHermite,ValPtsInterpY,ValDerivPtsInterp2Y)
YtChebyHH = algo.Horner(DD,ptsInterpHermite,tt)

import matplotlib.pyplot as plt



fig, axs = plt.subplots(3,2,figsize=(15,20))

#point d'interpolation
#axs[0,0].plot(ptsEqui,ptsInterpX,'k+')
#axs[1,0].plot(ptsEqui,ptsInterpY,'k+')
#axs[0,1].plot(ptsCheby,ptsInterpX,'r+')
#axs[1,1].plot(ptsCheby,ptsInterpY,'r+')

#point d"evaluation  x et y en fonction de t
#axs[0,0].plot(tt,XtEquiNA,'b-')
#axs[1,0].plot(tt,YtEquiNA,'b-')
#axs[0,1].plot(tt,XtChebyNA,'g-')
#axs[1,1].plot(tt,YtChebyNA,'g-')

#point d'evaluation x en fonction de y
axs[0,0].plot(XtEquiNA,YtEquiNA,'b-')
axs[0,1].plot(XtChebyNA,YtChebyNA,'g-')
axs[0,0].set_title('points équiréparties')
axs[0,1].set_title('points de Chebychev')
axs[0,0].set_ylabel("Neville Aitken")

axs[1,0].plot(XtEquiH,YtEquiH,'b')
axs[1,1].plot(XtChebyH,YtChebyH,'g')
axs[1,0].set_ylabel("DD + Horner")

axs[2,0].plot(XtEquiHH,YtEquiHH,'b')
axs[2,1].plot(XtChebyHH,YtChebyHH,'g')
axs[2,0].set_ylabel("DD + Horner + Hermite")

#plt.show()
plt.savefig("dessin3.pdf")
