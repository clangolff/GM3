import numpy as np
import matplotlib.pyplot as plt
N = 1000
x = np.linspace(0,1,N)
y = 6 * x * (1 - x)
a = 0
b = 1
M = 3/2
mu = 0.5
sigma2 = 0.15
Px = np.random.normal(mu,sigma2,N)
Py = M * np.random.uniform(0,1,N)
Pnt_statut = (Py <= 6 * Px * (1 - Px))
Pnt_accx = []
Pnt_accy = []
Pnt_rejx = []
Pnt_rejy = []
for i in range(N) :
	if Pnt_statut[i] ==True :
		Pnt_accx.append(Px[i])
		Pnt_accy.append(Py[i])
	else :
		Pnt_rejx.append(Px[i])
		Pnt_rejy.append(Py[i])

print("proba = ",len(Pnt_accx)/N)
fig, ax = plt.subplots()
plt.scatter(Pnt_rejx, Pnt_rejy, color = 'red',label = 'point rejeté')
plt.scatter(Pnt_accx, Pnt_accy, color = 'green', label = 'point accepté')
plt.xlim(0,1)
plt.ylim(0,3/2+0.1)
plt.plot(x,y,color = 'black')
ax.set_title('Simulation par rejet pour {} point tirés'.format(N))
plt.legend(loc = 'upper left', fontsize = 8)
plt.savefig('algorejetV2.svg')

plt.show()
