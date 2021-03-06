import scipy.misc as misc
import math
import numpy as np
import matplotlib.pyplot as plt

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

def rexp(lambduh): # lambduh mispelled to avoid clash with lambda in python
    # u = get value from U(0,1) then
    # return F^-1(u) for exp cdf F^-1
    u = runif01()
    return -math.log(1 - u)/lambduh

def exppdf(x, lambduh):
    return lambduh * math.exp(-lambduh * x)

def unifvar(a, b):
    return ((b-a)**2.0)/12.0

def normpdf(x, mu, sigma): # sigma is the standard deviation, sigma^2 is the variance
    # Accept either a floating-point number or a numpy ndarray, such as what you get
    # from arange(). You do not need a loop in the code does not change here
    # because 2 * ndarray is another ndarray automatically. In this respect,
    # numpy is very convenient and behaves like R.
    if isinstance(x, np.ndarray):
        return [1.0/(sigma * math.sqrt(2 * math.pi)) * math.exp(-((i-mu)**2)/(2*sigma**2.0)) for i in x]
    else:
        return 1.0/(sigma * math.sqrt(2 * math.pi)) * math.exp(-((x-mu)**2)/(2*sigma**2.0))

def rnorm01():
    # Return a value from N(0,1)
    N = 100

    X = [runif01() for i in range(N)]
    X_ = mean(X)
    rv = X_ - 0.5
    rv /= math.sqrt(var(X)/N)

    return rv

def rnorm(mean, variance):
    # Return a value from N(mean, variance)
    Z = rnorm01()
    X = Z * math.sqrt(variance) + mean

    return X
