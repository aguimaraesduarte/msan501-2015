from stats import *
import matplotlib.pyplot as plt
import time
import scipy.stats

setseed( int(round(time.time() * 1000)) )

tips = [20.8, 18.7, 19.1, 20.6, 21.9, 20.4, 22.8,
        21.9, 21.2, 20.3, 21.9, 18.3, 21.0, 20.3,
        19.2, 20.2, 21.1, 22.1, 21.0, 21.7]

m = mean(tips)
variance = var(tips)
stddev = math.sqrt(variance)
n = len(tips)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.axis([18, 23, 0, 0.45])
plt.hist(tips, bins=5, normed=1)
plt.title("Sample Tips After Free Beer", fontsize=16)
plt.xlabel("Tip %", fontsize=16)
plt.ylabel("Density", fontsize=16)
plt.text(18.25, 0.24, "Sample mean = %.2f" % m)
plt.show()
# Histogram not identical to the one shown on the pdf

x = np.arange(min(tips), max(tips), 0.01)
y = normpdf(x, 20.0, stddev/math.sqrt(n))

fig = plt.figure()
ax = fig.add_subplot(111)
plt.axis([18, 22, 0, 1.6])
plt.plot(x, y, color='red')
plt.title("Tips control ($H_0$) sample mean density $N(20.0, s^2/n)$", fontsize=16)
plt.xlabel("Average tip %", fontsize=16)
plt.ylabel("Density", fontsize=16)
plt.plot(m, 0, "D")
plt.text(m, 0.05, "Sample mean = %.2f" % m)
plt.show()

t = (m - 20.0)/(stddev/math.sqrt(n))
print "t-value = %f" % t
p = 2.0 * (1-scipy.stats.t.cdf(t, n-1))
print "p-value (t-test) = %f" % p

TRIALS = 5000
X = [[rnorm(20.0, variance) for i in range(n)] for j in range(TRIALS)]
X_ = [mean(X[i]) for i in range(TRIALS)]
#greater = np.sum(X_ >= np.mean(tips))
greater = sum([x >= mean(tips) for x in X_])
p2 = (2.0 * greater)/TRIALS

print "p-value (bootstrap) = %f" % p2

# Write values to output file
output = open("hyp_results.txt", "w")
output.write("t-value = %f\n" % t)
output.write("p-value (t-test) = %f\n" % p)
output.write("p-value (bootstrap) = %f\n" % p2)
output.close()