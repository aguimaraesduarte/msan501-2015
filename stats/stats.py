import scipy.misc as misc

def mean(x):
    s = 0
    for i in range(len(x)):
        s += x[i]
    return s * 1.0/len(x)

def var(x):
    m = mean(x)
    s = 0
    for i in range(len(x)):
        s += (x[i] - m)**2.0
    return s/(len(x)-1)

def cov(x, y):
    if len(x) != len(y):
        return 0
    else:
        xbar = mean(x)
        ybar = mean(y)
        s = 0
        for i in range(len(x)):
            s += (x[i] - xbar) * (y[i] - ybar)
        return s * 1.0/(len(x)-1)

# Global variables
m = 2**31 - 1
a = 7**5
x0 = 666

# U(0,1)
def runif01():
    global x0
    setseed(a * x0 % m)
    return x0 * 1.0/m

# U(a,b)
def runif(x1,x2):
    return runif01() * (x2-x1) + x1

def setseed(s): #updates the seed global variable
    global x0
    x0 = s

def binomial(n,p):
    # Sim with prob p, n bernoulli trials; return number of successes
    count = 0
    for i in range(n):
        if runif01() < p:
            count += 1
    return count

def binom(n, k, p):
    # If we run n trials with p prob for each trial of success,
    # what is probability of having k successes? You can use scipy.misc.comb() if you want.
    return misc.comb(n,k) * p**k * (1.0-p)**(n-k)