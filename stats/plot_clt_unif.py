from stats import *

import time
import matplotlib.pyplot as plt
import numpy as np

setseed( int(round(time.time() * 1000)) )

N = 20
TRIALS = 2000

X = [[runif01() for n in range(N)] for t in range(TRIALS)]
X_ = [mean(X[i]) for i in range(TRIALS)]

x = np.arange(min(X_), max(X_), 0.01)
Y = normpdf(x, 0.5, math.sqrt(1.0/(12*N)))

fig = plt.figure()
ax = fig.add_subplot(111)
plt.hist(X_, bins=40, normed=1)
plt.axis([0.1, 0.9, 0, 7])
plt.plot(x, Y, color='red')

plt.text(.02,.9, '$N = %d$' % N, transform = ax.transAxes)
plt.text(.02,.85,'$TRIALS = %d$' % TRIALS, transform = ax.transAxes)
plt.text(.02,.8, 'mean($\\overline{X}$) = %f' % np.mean(X_), transform = ax.transAxes)
plt.text(.02,.75,'var($\\overline{X}$) = %f' % np.var(X_), transform = ax.transAxes)
plt.text(.02,.7, 'var U($0,1$)/%d = %f' % (N,unifvar(0,1)/N), transform = ax.transAxes)
plt.title("CLT Density Demo. sample mean of U(0,1) is $N(.5, \sigma^2/N)$")
plt.xlabel("$\\overline{X}$", fontsize=16)
plt.ylabel("Density", fontsize=16)
plt.savefig('clt_unif-%d-%d.pdf' % (TRIALS, N), format="pdf")
plt.show()
