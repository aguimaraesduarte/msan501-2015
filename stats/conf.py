from stats import *
import matplotlib.pyplot as plt
import time

setseed( int(round(time.time() * 1000)) )

def samples(data):
    # Return a random sample of data values with replacement.
    # The returned array has same length as data

    indexes = [int(runif(0, len(data))) for t in range(len(data))]
    return [data[i] for i in indexes]

prices = []
f = open("prices.txt")
for line in f:
    v = float(line.strip())
    prices.append(v)

TRIALS = 500
X = [samples(prices) for t in range(TRIALS)]
X_ = [mean(x) for x in X]

sorted_X_ = sorted(X_)
lower = 0.025*TRIALS
upper = 0.975*TRIALS
inside = [x for x in sorted_X_[int(lower):int(upper)]]

#print inside[0], inside[-1]

fig = plt.figure()
ax = fig.add_subplot(111)
plt.axis([1.10, 1.201, 0, 30])

plt.plot(inside[0], 0, 'D')
plt.plot(inside[-1], 0, 'D')

x = np.arange(1.05, 1.25, 0.001)
mean = mean(X_)
stddev = math.sqrt(var(X_))
y = normpdf(x, mean, stddev)
plt.plot(x, y, color='red')

left = mean - 1.96*stddev
right = mean + 1.96*stddev
ci_x = np.arange(left, right, 0.001)
ci_y = normpdf(ci_x, mean, stddev)
plt.fill_between(ci_x, ci_y, color="#F8ECE0")

plt.text(.02,.95, '$TRIALS = %d$' % TRIALS, transform = ax.transAxes)
plt.text(.02,.9, '$mean(prices)$ = %f' % np.mean(prices), transform = ax.transAxes)
plt.text(.02,.85, '$mean(\\overline{X})$ = %f' % np.mean(X_), transform = ax.transAxes)
plt.text(.02,.80, 'stddev(\\overline{X})$ = %f' %
         np.std(X_,ddof=1), transform = ax.transAxes)
plt.text(.02,.75, '95%% CI = $%1.2f \\pm 1.96* %1.3f$' %
         (np.mean(X_),np.std(X_,ddof=1)), transform = ax.transAxes)
plt.text(.02,.70, '95%% CI = ($%1.2f,\\ %1.2f$)' %
         (np.mean(X_)-1.96*np.std(X_),
          np.mean(X_)+1.96*np.std(X_)),
         transform = ax.transAxes)

plt.text(1.135, 11.5, "Expected", fontsize=16)
plt.text(1.135, 10, "95% CI $\\mu \\pm 1.96\\sigma$", fontsize=16)
plt.title("95% Confidence Intervals: $\\mu \\pm 1.96\\sigma$", fontsize=16)
ax.annotate("Empirical 95% CI",
            xy=(inside[0], .3),
            xycoords="data",
            xytext=(1.13,4), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            fontsize=16)
plt.savefig('conf-%d.pdf' % TRIALS, format = 'pdf')
plt.show()


