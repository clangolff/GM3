import numpy as np
import matplotlib.pyplot as plt

Nmax = 200

A = np.eye(Nmax,Nmax,k=-1)*-1 + np.eye(Nmax,Nmax,)*2 + np.eye(Nmax,Nmax,k=1)*-1

print("Cond(A) = " , np.linalg.cond(A))

b = np.zeros(Nmax)
             
x0 = np.sum(A,axis=0)
r0 = b - np.matmul(A,x0)


def gradConj(Nmax,tol,A,X,R0):
    ité = 0
    d = R0
    normeR0 = np.matmul(R0.T,R0)
    evolution_residu = np.array([normeR0])
   
    for k in range(Nmax) :
        ité += 1
        Ad = np.matmul(A,d)
        alpha = normeR0 / np.matmul(d.T,Ad)
        X = X + alpha * d
      
        R1 = R0 - alpha * Ad
        normeR1 = np.matmul(R1.T,R1)
        evolution_residu=np.vstack((evolution_residu,[normeR1]))
        if normeR1 < tol :
            break
        beta = normeR1 / normeR0
        d = R1 + beta * d
        R0 = R1
        normeR0 = normeR1
       
    return  evolution_residu, ité


Rsucc, ité = gradConj(Nmax,1e-10,A,x0,r0)    #tableau des valeurs de X et residu au fur est à mesure de l'algo

normeResidu = Rsucc[:,0]

fig = plt.figure(figsize=plt.figaspect(1.))
ax = fig.add_subplot(1, 1, 1)

ax.plot([k for k in range(ité+1)],normeResidu,'ko')
ax.set_xlabel("itérations")
ax.set_ylabel("norme résidu au carré")
ax.set_yscale('log')
plt.show()
