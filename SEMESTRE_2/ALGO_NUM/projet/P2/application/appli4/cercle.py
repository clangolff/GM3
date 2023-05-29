import numpy as np

#récupération des données
data = np.loadtxt('data', delimiter = " ")

#dimension A
n = 3
N = 4

#Formatage des données 
x1 = data[:,0]
x2 = data[:,1]
g  = data[:,2]


x1 = np.array([x1]).T
x2 = np.array([x2]).T

un = np.array([np.ones(4)]).T

A = np.concatenate((x1, x2,un) , axis = 1)

Y = np.array([g]).T

#décomposition QR
Q,R = np.linalg.qr(A,'complete')

Y = np.matmul(Q.T,Y)

#récupération système
R1 = R[0:n,0:n]
c = Y[0:n]

#résolution système
coeff = np.linalg.solve(R1,c)
coeff = coeff[:,0]

#erreur
d = Y[n::]
d = d[:,0]
err = np.linalg.norm(d)

a = coeff[0] * -0.5
b = coeff[1] * -0.5
r = np.sqrt(a**2 + b**2 - coeff[2])

with open("lambda",'w') as fichier :
    fichier.write("Lambda 1, 2 et 3 :\n")
    fichier.write(str(coeff[0]))
    fichier.write(" ")
    fichier.write(str(coeff[1]))
    fichier.write(" ")
    fichier.write(str(coeff[2]))
    fichier.write("\n")
    fichier.write("Coordonnées du centre du cercle et son rayon :\n")
    fichier.write(str(a))
    fichier.write(" ") 
    fichier.write(str(b))
    fichier.write(" ")
    fichier.write(str(r))
    fichier.write("\n")
    fichier.write("erreur\n")
    fichier.write(str(err))
