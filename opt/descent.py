import numpy as np

def minimize(f, x0, eta, h, precision):
    tracex = []
    tracex.append(x0) # add a starting position

    xold = x0
    fderiv = f(xold + h) - f(xold)
    xnew = xold - eta*fderiv

    while abs(f(xnew) - f(xold)) > precision:
        tracex.append(xnew)
        xold = xnew
        fderiv = f(xold + h) - f(xold)
        xnew = xold - eta * fderiv

    tracex.append(xnew)

    return tracex

def f(x):
    if isinstance(x, np.ndarray):
        return [np.cos(3*np.pi*t)/t for t in x]
        #return [5 * i ** 3 + 2 * i ** 2 - 3 * i for i in x]
        #return [(i - 2) ** 2 + 1 for i in x]
    else:
        return np.cos(3*np.pi*x)/x
        #return 5 * x ** 3 + 2 * x ** 2 - 3 * x
        #return (x - 2) ** 2 + 1