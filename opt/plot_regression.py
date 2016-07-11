from pylab import show, text
import time

from regression import *

# Average hourly wage
HOURLY_WAGE = [2.98, 3.09, 3.23, 3.33, 3.46, 3.6, 3.73, 2.91, 4.25, 4.47, 5.04, 5.47, 5.76]
# Number of homicides per 100,000 people
MURDERS = [8.6, 8.9, 8.52, 8.89, 13.07, 14.57, 21.36, 28.03, 31.49, 37.39, 46.26, 47.24, 52.33]

a, b = np.polyfit(HOURLY_WAGE, MURDERS,  1) #fit y = a*x + b
seq_x = np.arange(min(HOURLY_WAGE)-1, max(HOURLY_WAGE)+1, 0.01)
ablineValues = [a*x+b for x in seq_x]
fig = plt.figure()
plt.plot(HOURLY_WAGE, MURDERS, 'ko')
plt.plot(seq_x, ablineValues, 'b--')
plt.axis([2.8, 6.0, 7, 54])
plt.title("Fit $y=%.3fx%.3f$" % (a, b))
plt.xlabel("Average hourly wage", fontsize=16)
plt.ylabel("# murders per 100,000 people", fontsize=16)
plt.show()

B0 = [-41, 10]
LEARNING_RATE = 2.0
h = 0.001
PRECISION = 0.0000001

def Cost(B, X=HOURLY_WAGE, Y=MURDERS):
    cost = 0.0
    for i in xrange(0, len(X)):
        cost += (B[1]*X[i] + B[0] - Y[i])**2.0
    return cost

def heatmap(X, Y, f, trace=None): # trace is a list of [b1, b2] pairs
    C = np.matrix()
    imshow(C, origin='lower',
           extent = [min(b1), max(b1), min(b2), max(b2)],
           vmax = abs(C).max(),
           vmin = -abs(C).max()
           )
    plot(p[0], p[1], "ko", markersize=1)

    return -1

random.seed(int(round(time.time() * 1000)))

begin = time.time()
(m,steps,trace) = minimize(Cost, B0, LEARNING_RATE, h, PRECISION)
end = time.time()

heatmap(HOURLY_WAGE, MURDERS, Cost, trace)

show()
