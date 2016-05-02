from filter import *

def laplace(data):
    return data[1]+data[2]+data[3]+data[4]-4*data[0]

def minus(A, B):
    width, height = A.size
    matrixA = A.load()
    matrixB = B.load()
    imgdup = A.copy()
    m = imgdup.load()

    for x in range(width):
        for y in range(height):
            m[x, y] = matrixA[x, y] - matrixB[x, y]

    return imgdup

img = open(sys.argv)
img.show()
laplace = filter(img, laplace)
replace = minus(img, laplace)
replace.show()