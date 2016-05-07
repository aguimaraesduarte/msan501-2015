def sqrt(n, x0 = 1, iter = 50):
    res = x0
    for i in range(iter):
        res = 0.5 * (res + n/res)
    return res