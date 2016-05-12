from descent import *
import matplotlib.pyplot as plt
import random

x0_1 = random.random()*1.1+0.1
x0_2 = random.random()*1.1+0.1
ETA = 2
STEP = 0.001
PRECISION = 0.0000001

tracex_1 = minimize(f, x0_1, ETA, STEP, PRECISION)
tracex_2 = minimize(f, x0_2, ETA, STEP, PRECISION)
tracey_1 = [f(x) for x in tracex_1]
tracey_2 = [f(x) for x in tracex_2]
graphx = np.arange(.1,1.1,0.01)
graphy = f(graphx)

fig = plt.figure()
plt.plot(graphx,graphy)
plt.plot(tracex_1, tracey_1, 'ro') # plot red dots
plt.plot(tracex_2, tracey_2, 'go') # plot green dots
plt.axis([0, 1.1, -4, 6])
plt.text(0.25, 4, "f(%.5f) = %.9f\nsteps = %d" %
         (tracex_1[-1], tracey_1[-1], len(tracex_1)),
         color='red', fontsize=16)
plt.text(0.25, 2.75, "f(%.5f) = %.9f\nsteps = %d" %
         (tracex_2[-1], tracey_2[-1], len(tracex_2)),
         color='green', fontsize=16)
#plt.savefig("traces.pdf", format="pdf")
plt.show()