import numpy as np
import matplotlib.pyplot as plt

Nmax = 200

A = np.eye(Nmax,Nmax,k=-1)*-1 + np.eye(Nmax,Nmax,)*2 + np.eye(Nmax,Nmax,k=1)*-1

print("Cond(A) = " , np.linalg.cond(A))

b = np.zeros(Nmax)
             
x0 = np.sum(A,axis=0)
r0 = b - np.matmul(A,x0)



def descente(Nmax,tol,A,b,X):
    ité = 0
    w = b - np.matmul(A,X)    #direction de descente -> le gradient (résidu)
    
    normeR = np.matmul(w.T,w)
    evolution_residu = np.array([normeR])

    for k in range(Nmax) :
        ité += 1
        Aw = np.matmul(A,w)
        z = normeR / np.matmul(w.T,Aw)
        X = X + z * w
      
        w = b - np.matmul(A,X)
        normeR = np.matmul(w.T,w)
        evolution_residu=np.vstack((evolution_residu,[normeR]))
        if normeR < tol :
            break
       
    return  evolution_residu, ité

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
    
Rsucc1, ité1 = descente(Nmax,1e-10,A,b,x0)    #tableau des valeurs de X et residu au fur est à mesure de l'algo
Rsucc2, ité2 = gradConj(Nmax,1e-10,A,x0,r0)

normeResidu1 = Rsucc1[:,0]
normeResidu2 = Rsucc2[:,0]

fig = plt.figure(figsize=plt.figaspect(1.))
ax = fig.add_subplot(1, 1, 1)

ax.plot([k for k in range(ité1+1)],normeResidu1,'bo',markersize=2)
ax.plot([k for k in range(ité2+1)],normeResidu2,'ro',markersize=2)
ax.grid('True')
ax.set_xlabel("itérations")
ax.set_ylabel("norme résidu au carré")
ax.set_yscale('log')
plt.show()
