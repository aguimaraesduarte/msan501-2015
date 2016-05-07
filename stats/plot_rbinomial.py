from stats import *

import time
import matplotlib.pyplot as plt

setseed( int(round(time.time() * 1000)) )

n = 500
p = 0.4
samples = 5000
X = [binomial(n,p) for t in range(samples)]
Y = [binom(n, k, p) for k in range(0,n+1,5)]

fig = plt.figure()
ax = fig.add_subplot(111)
plt.hist(X, normed=1)
plt.bar(range(0,n+1,5), Y, color='red', align='center', width=1)
plt.axis([150,250,0,.05]) # set the axes so that we get a close-up
plt.text(160,0.04, '$n = %d$' % n, fontsize=16)
plt.text(160,0.037, '$p = %f$' % p, fontsize=16)
plt.text(160,0.034, '$SAMPLES = %d$' % samples, fontsize=16)
plt.savefig('binom_500_0.4.pdf', format="pdf")
plt.show()