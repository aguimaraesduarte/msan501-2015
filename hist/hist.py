import matplotlib.pyplot as plt
import numpy as np

N = 1000
rangeStart = 2
rangeEnd = 8
X = [np.random.uniform(rangeStart,rangeEnd) for i in range(N)] # U(rangeStart, rangeEnd)
# or np.random.uniform(rangeStart,rangeEnd,N)

fig = plt.figure() # get a handle on the figure object itself
ax = fig.add_subplot(111) # weird stuff to get the Axes object within the figure
plt.hist(X, normed=1)
plt.title("U(" + str(rangeStart) + "," + str(rangeEnd) + ") Density Demo")
plt.xlabel("X", fontsize=16)
plt.ylabel("Density", fontsize=16)
plt.axis([1, 9 , 0, 0.25])
# put N=... at top left
plt.text(.1,.9, 'N = %d' % N, fontsize=16, transform = ax.transAxes)
plt.savefig('unif-2-8-density-fancy.pdf', format="pdf")
plt.show()