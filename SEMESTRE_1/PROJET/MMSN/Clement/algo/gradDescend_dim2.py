import numpy as np
import matplotlib.pyplot as plt

A = np.eye(2,2,k=-1)*-1 + np.eye(2,2)*2 + np.eye(2,2,k=1)*-1

print("Cond(A) = " , np.linalg.cond(A))

b = np.array([[1],
             [1]])
             
x0 = np.array([[ -5],
               [-10]])
r0 = b - np.matmul(A,x0)

def J(x,y,A,b) :
    return 0.5*A[0,0]*x*x+A[0,1]*x*y+0.5*A[1,1]*y*y -b[0]*x-b[1]*y 

x,y = np.mgrid[-10:10:0.5,-10:10:0.5]
z = J(x,y,A,b)

def descente(Nmax,tol,A,b,X):
    ité = 0
    w = b - np.matmul(A,X)    #direction de descente -> le gradient (résidu)
    
    normeR = np.matmul(w.T,w)
    evolution_residu = np.array([normeR])
    evolution_X = [[X[0],X[1]]]
    for k in range(Nmax) :
        ité += 1
        Aw = np.matmul(A,w)
        z = normeR / np.matmul(w.T,Aw)
        X = X + z * w
        evolution_X = np.vstack((evolution_X,[[X[0],X[1]]]))
        w = b - np.matmul(A,X)
        normeR = np.matmul(w.T,w)
        evolution_residu=np.vstack((evolution_residu,[normeR]))
        if normeR < tol :
            break
       
    return evolution_X , evolution_residu, ité

Nmax = 10
Xsucc, Rsucc, ité = descente(Nmax,1e-10,A,b,x0)    #tableau des valeurs de X et residu au fur est à mesure de l'algo

X1 = Xsucc[:,0]    #coordonnée x
X2 = Xsucc[:,1]    #coordonnée y
normeResidu = Rsucc[:,0]
print(normeResidu)


fig = plt.figure(figsize=plt.figaspect(1.))
ax = fig.add_subplot(2, 2, 1)
contours = ax.contour(x,y,z,30)
ax.plot(X1,X2,'k-o')

ax = fig.add_subplot(2, 2, 2)

ax.plot([k for k in range(ité+1)],normeResidu)
ax.set_xlabel("itérations")
ax.set_ylabel("norme résidu au carré")

ax = fig.add_subplot(2, 2, 3, projection='3d')
surf = ax.contour(x,y,z,50)
plt.show()
