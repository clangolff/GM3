import numpy as np

#recuperation données
data = np.loadtxt('data', delimiter = " ")


#dimension matrice A
n = 2
N = 4

#formatage des données
x1 = data[:,0]
x2 = data[:,1]
g  = data[:,2]

x1 = np.log(x1.T)
x2 = np.log(x2.T)
g  = np.log(g.T)

x1 = np.array([x1]).T
x2 = np.array([x2]).T

Y = np.array([g]).T

A = np.concatenate((x1, x2) , axis = 1)


#decompostion QR de A
Q,R = np.linalg.qr(A, 'complete')
Y = np.matmul(Q.T,Y)

#recuperation systeme à resoudre
R1=R[0:n,0:n]
c = Y[0:n]
#solution systeme
coeff =  np.linalg.solve(R1,c)
coeff = coeff[:,0]

#erreur
d = Y[n::]
d = d[:,0]
err = np.linalg.norm(d)



with open("lambda",'w') as fichier :
    fichier.write("Lambdas 1 et 2 : \n")
    fichier.write(str(coeff[0]))
    fichier.write(" ")
    fichier.write(str(coeff[1])) 
    fichier.write("\nErreur au sens des moindres carrés : \n")
    fichier.write(str(err))


