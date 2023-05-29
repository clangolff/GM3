import scipy.stats
import numpy as np
import matplotlib.pyplot as plt

mu = 0.5
sigma2 = 0.15

x1 = np.linspace(0,1,50)
fx = 6 * x1 * (1 - x1)
x2 = np.linspace(-5,5,200)
gx = scipy.stats.norm.pdf(x2,mu,sigma2)
fig,ax = plt.subplots()
plt.plot(x1,fx,color = 'green', label = 'f(x)')
plt.plot(x2, gx,color = 'red',label = 'N({};{})'.format(mu,sigma2))

plt.xlim(-1,2)
plt.ylim(-0.02,2)
plt.grid()
plt.legend()
ax.set_title("loi normale sur la coordonné x")
plt.savefig('graphe_loi_normal.svg')
plt.show()

