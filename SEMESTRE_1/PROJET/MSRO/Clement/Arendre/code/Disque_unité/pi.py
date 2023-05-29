import numpy as np
import matplotlib.pyplot as plt

N = 1000
angle = np.linspace(0 , 2 * np.pi , 50)

def experiencePi(N) : 
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
	return 4*(len(x_int) / len(x))
PiExperimental = [experiencePi(N) for i in range(1000)]
moyennePi = np.mean(PiExperimental)
ecarttypePi = np.std(PiExperimental)

fig, ax = plt.subplots()

plt.hist(PiExperimental, range = (2.9,3.4), bins = 100, color = 'green', label ="1000 tirages", edgecolor = 'black')
plt.text(2.9,55,"moyenne = {:.2f}".format(moyennePi))
plt.text(2.9,52,"écart-type = {:.2f}".format(ecarttypePi))
ax.set_xlabel("valeur de pi")
ax.set_ylabel("nombre de mesures")
plt.savefig("pi.svg")
plt.show()
