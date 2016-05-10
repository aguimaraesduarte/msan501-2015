from stats import *

import time
import matplotlib.pyplot as plt
import numpy as np

setseed( int(round(time.time() * 1000)) )

N = 1000
LAMBDUH = 1.5

X = [rexp(LAMBDUH) for t in range(N)]

x = np.arange(0, 6, 0.01)
Y = [exppdf(i, LAMBDUH) for i in x]

fig = plt.figure()
plt.hist(X, bins=40, normed=1)
plt.plot(x, Y, color='red')
plt.savefig('exp-%d-%.1f.pdf' % (N, LAMBDUH), format="pdf")
plt.show()