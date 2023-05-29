import numpy as np
import matplotlib.pyplot as plt

Nmax = int(input("entrer dimension A\n"))

tol = 1.e-6
res = []
ité = []
X = np.random.rand(Nmax)
#X = np.array([[5],[-8]])
A = np.eye(Nmax,Nmax,k=-1)*-1 + np.eye(Nmax,Nmax)*2 + np.eye(Nmax,Nmax,k=1)*-1


b = np.ones(Nmax)

R0 = b - np.matmul(A,X)
d = R0


for k in range(Nmax) : 
	normeR0 = np.matmul(R0.T,R0)
	ité.append(k) 
	res.append(normeR0)
	
	alpha =  normeR0 / np.matmul(d.T,np.matmul(A,d))
	X = X + alpha * d
	R1 = R0 -  alpha * np.matmul(A,d)
	normeR1 = np.matmul(R1.T,R1) 
	beta = normeR1 / normeR0

	if normeR1 < tol : 
		break
	d = R1 + beta * d
	R0 = R1
	
print(X)                                 #solution du gradient conjugué
print(np.linalg.solve(A,b))      #solution de la librairie numpy

plt.plot(ité,res)
plt.show()
