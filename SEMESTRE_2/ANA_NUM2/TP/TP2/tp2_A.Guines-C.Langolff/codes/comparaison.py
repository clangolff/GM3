#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt

import algo
import data

# Intervalle d'intégration
# Modifier ICI :
a=0.0
b=0.75

# p-sous intervalles pour la formule de quadrature (composite) :
# Modifier ICI :
p = 3
   
resQuadTrap = 0.0
resQuadGauss = 0.0
resQuadHerm = 0.0

resQuadTrap = algo.quadTrap(a,b,p,data.f)

resQuadGauss = algo.quadGauss(a,b,p,data.f)

resQuadHerm = algo.quadHerm(a,b,p,data.f,data.df)
     

################# AFFICHAGE ######################
f = data.f

fig, axs = plt.subplots(3,figsize=(10,20))

h = (b-a)/p
xx = np.arange(a,b,max(h*0.01,1e-3))
yy = f(xx)
    
axs[0].plot(xx,yy, '-',color='#2ca02c',linewidth=2.0)
axs[1].plot(xx,yy, '-',color='#2ca02c',linewidth=2.0)
axs[2].plot(xx,yy, '-',color='#2ca02c',linewidth=2.0)        
           
x = a

while(x < b-1e-8):

	#Trapèze
        plt.plot([x],[f(x)],'x',color='#ff7f0e')
        axs[0].plot([x,x+h],[f(x),f(x+h)],'--',color='#1f77b4',linewidth=2.0)
        axs[0].plot([x,x],[0.0,f(x)],'k--',linewidth=1.0)
        axs[0].plot([x],[f(x)],'x',color='#ff7f0e')
        axs[0].plot([b],[f(b)],'x',color='#ff7f0e')

	#Gauss
        xhG = np.arange(x,x+h+h*0.01,h*0.1)
        x1G = x+h*(1.0-1.0/np.sqrt(3.0))*0.5
        x2G = x+h*(1.0+1.0/np.sqrt(3.0))*0.5
        yhG = f(x1G) * (xhG-x2G) / (x1G-x2G)
        yhG += f(x2G) * (xhG-x1G)/ (x2G-x1G)
            
        axs[1].plot(xhG,yhG,'--',color='#1f77b4',linewidth=2.0)
        axs[1].plot([x,x],[0.0,f(x)],'k--',linewidth=1.0)
        axs[1].plot([x1G,x2G],[f(x1G),f(x2G)],'x',color='#ff7f0e')
        axs[1].plot([b],[f(b)],'x',color='#ff7f0e')

	#Hermite
        xhH = np.arange(x,x+h+h*0.01,h*0.1)
        x1H = x+h*0.5
        yhH = f(x1H) + 0*xhH
        x0H = x
        x2H = x+h
        df0 = data.df(x0H)
        df1 = data.df(x1H)
            
        aa = 0.5*(df0 + df1)
        bb = 0.5*(df1 - df0)/h
        yhH += (xhH - x1H)*aa + ((xhH-x1H)**2)*bb
        axs[2].plot(xhH,yhH,'--',color='#1f77b4',linewidth=2.0)
        axs[2].plot([x,x],[0.0,f(x)],'k--',linewidth=1.0)
        axs[2].plot([x1H],[f(x1H)],'x',color='#ff7f0e')
            
        x = x+h

#axs[0].plot([b,b],[0.0,f(b)],'k--',linewidth=1.0)
#axs[1].plot([b,b],[0.0,f(b)],'k--',linewidth=1.0)
#axs[2].plot([b,b],[0.0,f(b)],'k--',linewidth=1.0)
 
#for i in range(1):
#    axs[i].plot([b,b],[0.0,f(b)],'k--',linewidth=1.0)
#    axs[i] = plt.gca()
 #   axs[i].set_xlim(a-0.1,b+0.1)
  #  axs[i].set_ylim(min(min(yy),0.0)-0.1,max(max(yy),0.0)+0.1)
   # # turn off the right spine/ticks
    #axs[i].spines['right'].set_color('none')
   # axs[i].yaxis.tick_left()

    # set the y-spine
    #axs[i].spines['bottom'].set_position('zero')

    # turn off the top spine/ticks
    #axs[i].spines['top'].set_color('none')
    #axs[i].xaxis.tick_bottom()


       
plt.legend(["f","Interp"])   
    
plt.show()
plt.savefig("comparaisonABS15.pdf")


