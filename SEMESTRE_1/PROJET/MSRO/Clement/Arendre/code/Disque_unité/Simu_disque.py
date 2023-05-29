import numpy as np
import matplotlib.pyplot as plt

N = 1000
def traceCercle() :
	angle = np.linspace(0 , 2 * np.pi , 50)
	plt.plot(np.cos(angle) , np.sin(angle) , color = 'black')
 
def traceCarré(ax) :
	carré = plt.Rectangle((-1,-1),2,2, edgecolor = "black", fill = False)
	ax.add_patch(carré)

x = np.random.uniform(-1,1,N)
y = np.random.uniform(-1,1,N)
x_ext = []
x_int = []
y_ext = []
y_int = []

for i in range (N) :	
    if (x[i]*x[i] + y[i]*y[i]) <= 1 :
        x_int.append(x[i])
        y_int.append(y[i])
    else :
        x_ext.append(x[i])
        y_ext.append(y[i])


proba = (len(x_int) / len(x))
print(proba)
fig, ax = plt.subplots()
plt.scatter(x_int, y_int, color = 'green',label = "points acceptés")
plt.scatter(x_ext, y_ext, color = 'red', label = "points rejetés")
traceCercle()
traceCarré(ax)
plt.axis('equal')
ax.set_title('simulation pour {} points tirés'.format(N))
plt.legend(loc = 'best', fontsize = 8)
plt.axis('off')
plt.savefig('Simu_disque.svg')
plt.show()
