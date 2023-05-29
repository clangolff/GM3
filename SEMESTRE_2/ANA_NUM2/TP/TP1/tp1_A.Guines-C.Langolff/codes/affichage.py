#!/usr/bin/python3
#-*- coding: utf-8 -*-

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
    
##----------------------------------
#  Affichage 1D :        
def afficher1D(list_x,list_y):
    #plt.hold(True)
    
    plt.plot(list_x[0],list_y[0], '-',linewidth=2.0)
    plt.plot(list_x[1],list_y[1], 'x',linewidth=4.0)
    #plt.plot(list_x[2],list_y[2], '--',linewidth=2.0)
    
    #plt.legend(["interp","(x_i,y_i)"])
    plt.legend(["interp","(x_i,y_i)","f"])
    #plt.axis('equal')
    axes = plt.gca()
    axes.set_xlim(min(list_x[1])-0.5,max(list_x[1])+0.5)
    #axes.set_ylim(min(list_y[1])-0.5,max(list_y[1])+0.1)
    #axes.set_ylim(-1.1,1.1)
    #axes.set_xlim(-0.1,1.1)
    axes.spines['left'].set_position('zero')

    # turn off the right spine/ticks
    axes.spines['right'].set_color('none')
    axes.yaxis.tick_left()

    # set the y-spine
    axes.spines['bottom'].set_position('zero')

    # turn off the top spine/ticks
    axes.spines['top'].set_color('none')
    axes.xaxis.tick_bottom()
    
    
    
    plt.show()
    #plt.hold('off')
##----------------------------------   

##----------------------------------
#  Affichage 1D :        
def afficher1Dbis(list_x,list_y):
    #plt.hold('on')
    
    plt.plot(list_x[0],list_y[0], '-',color='tab:blue',linewidth=2.0)
    plt.plot(list_x[1],list_y[1], '-',color='tab:red',linewidth=2.0)
    plt.plot(list_x[2],list_y[2], 'x',color='tab:blue',linewidth=4.0)
    plt.plot(list_x[3],list_y[3], 'x',color='tab:red',linewidth=4.0)
    
    plt.legend(["interp Xt","interp Yt","XX","YY"])
    plt.show()
    #plt.hold('off')
##----------------------------------    
    
    
