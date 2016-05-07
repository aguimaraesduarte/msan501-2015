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
