from stats import *

import time
import matplotlib.pyplot as plt

setseed( int(round(time.time() * 1000)) )

N = 1000
LAMBDUH = 1.5

X = [rexp(LAMBDUH) for t in range(N)]
inc = [x/10.0 for x in range(71)]
Y = [exppdf(x, LAMBDUH) for x in inc]

fig = plt.figure()
ax = fig.add_subplot(111)
plt.hist(X, bins=40, normed=1)
plt.plot(inc, Y, color='red')
plt.savefig('exp-%d-%.1f.pdf' % (N, LAMBDUH), format="pdf")
plt.show()