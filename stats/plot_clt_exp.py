from stats import *

import time
import matplotlib.pyplot as plt
import numpy as np

setseed( int(round(time.time() * 1000)) )

N = 10
TRIALS = 4000
LAMBDUH = 1.5

X = [[rexp(LAMBDUH) for n in range(N)] for t in range(TRIALS)]
X_ = [mean(X[i]) for i in range(TRIALS)]

inc = [x for x in np.linspace(0, 1, TRIALS)]
Y = [normpdf(x, LAMBDUH**(-1.0), math.sqrt((LAMBDUH**(-2.0))/N)) for x in inc]

fig = plt.figure()
ax = fig.add_subplot(111)
plt.hist(X_, bins=40, normed=1)
plt.plot(inc, Y, color='red')

plt.text(.02,.9, '$N = %d$' % N, transform = ax.transAxes)
plt.text(.02,.85, '$TRIALS = %d$' % TRIALS, transform = ax.transAxes)
plt.text(.02,.8, 'mean($\\overline{X}$) = %f' % np.mean(X_), transform = ax.transAxes)
plt.text(.02,.75, 'var($\\overline{X}$) = %f' % np.var(X_), transform = ax.transAxes)
plt.text(.02,.7, 'mean Exp($%f$) = %f' % (LAMBDUH,1/LAMBDUH), transform = ax.transAxes)
plt.text(.02,.65, 'var Exp($%f$)/%d = %f' % (LAMBDUH,N,(1/LAMBDUH**2)/N), transform = ax.transAxes)
plt.title("CLT Density Demo. sample mean of Exp($\lambda=1.5$) is $N(1/\lambda, (1/\lambda^2)/N)$")
plt.xlabel("$\\overline{X}$", fontsize=16)
plt.ylabel("Density", fontsize=16)
plt.axis([0,1.333,0,7])
plt.savefig('clt_exp-%d-%d.pdf' % (TRIALS, N), format="pdf")
plt.show()
