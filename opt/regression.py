import numpy as np
from pylab import imshow, plot
import matplotlib.pyplot as plt
import random

def minimize(f, B0, eta, h, precision):
    trace = []
    B = B0
    steps = 0 
    while True:
        steps += 1
        if steps % 10 == 0: # only capture every 10th value
            trace.append(B)
        C = [f([B[0]+h, B[1]]) - f(B), f([B[0], B[1]+h]) - f(B)]
        Bnew = [B[0]-eta*C[0], B[1]-eta*C[1]]

        if abs(f(Bnew) - f(B)) < precision and f(Bnew) > f(B):
            break

        B = Bnew

    return B, steps, trace
