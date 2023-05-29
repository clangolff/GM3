import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

def produit_scalaire(x1,x2,n):
    s = 0.
    for i in range (n):
        s += x1[i] * x2[i]
    return(s)

def somme_vectorielle(x1,x2,n):
    x = [0. for i in range(n)]
    for i in range(n):
        x[i] = x1[i] + x2[i]
    return(x)

def mult_matrice(A,x,n):        #multiplication d'un vecteur x par une matrice A
    t = [0. for i in range(n)]
    for i in range(n):
        for j in range(n):
            t[i] += A[i][j] * x[j]
    return(t)

def mult_scalaire(a,x,n):       #multiplication d'un vecteur x par un scalaire a
    for i in range (n):
        x[i] *= a
    return(x)

def algo_gradient_conjugue(x_k,p_k,r_k,n,tol):
        n1 = produit_scalaire(r_k,r_k,n)
        alpha_k = (n1)/produit_scalaire(mult_matrice(A,p_k,n),p_k,n)
        x_k = somme_vectorielle(x_k,mult_scalaire(alpha_k,p_k,n),n)
        r_k = somme_vectorielle(r_k,mult_scalaire(-alpha_k,mult_matrice(A,p_k,n),n),n)
        if(sqrt(produit_scalaire(r_k,r_k,n)) < tol):    #si norme2 de r_k < tol renvoyer x_k
            return(x_k)
        else :
            norme_r_k2 = produit_scalaire(r_k,r_k,n)
            n2 = produit_scalaire(r_k,r_k,n)
            beta_k = n1/n2
            p_k = somme_vectorielle(r_k, mult_scalaire(beta_k,p_k,n), n)
            algo_gradient_conjugue(x_k,p_k,r_k,n,tol)

n = int(input("dimension de l'espace : "))

A = [[0. for i in range(n)] for j in range(n)]
for i in range (n):
    A[i][i] = 2.
for i in range (n-1):
    A[i + 1][i] = -1.
    A[i][i + 1] = -1.

x_0 = [0. for i in range(n)]
print("rentrer valeurs de x_0 : ")
for i in range (n):
    x_0[i] = float(input())

b = [0. for i in range(n)]
print("rentrer valeurs de b : ")
for i in range (n):
    b[i] = float(input())

t = mult_matrice(A,x_0,n)
r_0 = [0. for i in range(n)]
for i in range (n):
    r_0[i] = b[i] - t[i]

p_0 = r_0

tol = float(input("valeur de la tolérance : "))

x = algo_gradient_conjugue(x_0,p_0,r_0,n,tol)
print(x)





