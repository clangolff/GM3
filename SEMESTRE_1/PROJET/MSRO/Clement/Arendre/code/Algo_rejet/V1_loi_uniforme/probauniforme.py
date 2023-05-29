import numpy as np
import matplotlib.pyplot as plt
N = 1000
x = np.linspace(0,1,N)
y = 6 * x * (1 - x)
a = 0
b = 1
M = 3/2 #max de la fonction

def ExperienceUniforme(N) :
	Px = a + (b - a) * np.random.uniform(0,1,N)
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
	return len(Pnt_accx)/N

ProbaUniforme = [ExperienceUniforme(N) for i in range(100)]

fig, ax = plt.subplots()
plt.hist(ProbaUniforme,bins = 50, edgecolor = 'black',color = "green")
#ax.set_title('Simulation par rejet pour {} point tirés'.format(N))
plt.text(0.63,7,'moyenne = {0:.2f}'.format(np.mean(ProbaUniforme)))
plt.text(0.63,6.5,'ecart-type = {0:.2f}'.format(np.std(ProbaUniforme)))
ax.set_title("probabilité d'avoir un point sous la fonction f pour 100 expériences")
plt.savefig('probaloiuniforme.svg')

plt.show()
