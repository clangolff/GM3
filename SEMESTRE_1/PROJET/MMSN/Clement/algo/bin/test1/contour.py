import numpy as np
import matplotlib.pyplot as plt

#A = np.array(   [[ 2 , 0 ],
#                 [ 0 , 3 ]])

b = np.array(   [[1],
                 [1]])


Nmax = int(input("entrer dimension A\n"))

tol = 1.e-6
res = []
ité = []
X = np.random.randn() * np.random.rand(Nmax)

A = np.eye(Nmax,Nmax,k=-1)*-1 + np.eye(Nmax,Nmax)*2 + np.eye(Nmax,Nmax,k=1)*-1

b = np.ones(Nmax)

R0 = b - np.matmul(A,X)
d = R0

evolution_rX_rY = [[R0[0],R0[1]]]

for k in range(Nmax) : 
	normeR0 = np.matmul(R0.T,R0)
	ité.append(k) 
	res.append(normeR0)
	
	alpha =  normeR0 / np.matmul(d.T,np.matmul(A,d))
	X = X + alpha * d
	R1 = R0 -  alpha * np.matmul(A,d)
	evolution_rX_rY =np.vstack((evolution_rX_rY , [[R1[0],R1[1]]]))
	normeR1 = np.matmul(R1.T,R1) 
	beta = normeR1 / normeR0

	if normeR1 < tol : 
		break
	d = R1 + beta * d
	R0 = R1

 
def J(x,y,A,b) :
    return A[0,0]*x*x + 2*A[0,1]*x*y + A[1,1]*y*y           # connerie ?

x , y = np.mgrid[-2.:2.:0.1, -2.:2.:0.1]

z = J(x,y,A,b)

rX = evolution_rX_rY[:,0]
rY = evolution_rX_rY[:,1]
print(rX,rY)
fig = plt.figure(figsize=plt.figaspect(2.))
ax = fig.add_subplot(2, 1, 1)
contours = ax.contour(x,y,z,30)
ax.plot(rX,rY,'k-o')

ax = fig.add_subplot(2, 1, 2, projection='3d')
surf = ax.contour(x,y,z,50)
plt.show()
