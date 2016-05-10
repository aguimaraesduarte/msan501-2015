from stats import *

import time
import matplotlib.pyplot as plt
import numpy as np

setseed( int(round(time.time() * 1000)) )

N = 100
TRIALS = 4000

X = [rnorm01() for t in range(TRIALS)]
plt.axis([-4, 7, 0, 0.5])
plt.hist(X, bins=40, normed=1)

x = np.arange(min(X), max(X), 0.01)
x = np.arange(-4, 6, 0.01)
MEAN = 0
VARIANCE = 1
y = normpdf(x, MEAN, math.sqrt(VARIANCE))

plt.plot(x, y, color='red')
plt.savefig('rnorm01-%d-%d.pdf' % (TRIALS, N), format = 'pdf')
plt.show()
