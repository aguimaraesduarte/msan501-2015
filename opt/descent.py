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
    else:
        return np.cos(3*np.pi*x)/x