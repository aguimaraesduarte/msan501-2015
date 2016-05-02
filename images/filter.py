import sys
from PIL import Image

def open(argv):
    if len(argv)<=1:
        print "missing image filename"
        sys.exit(1)

    img = Image.open(argv[1])
    img = img.convert("L") #make grayscale if not already (luminance)

    return img

def region3x3(img, x, y):
    me = getpixel(img, x, y)
    N = getpixel(img, x, y-1)
    NE = getpixel(img, x+1, y-1)
    E = getpixel(img, x+1, y)
    SE = getpixel(img, x+1, y+1)
    S = getpixel(img, x, y+1)
    SW = getpixel(img, x-1, y+1)
    W = getpixel(img, x-1, y)
    NW = getpixel(img, x-1, y-1)

    return [me, N, S, E, W, NE, SE, NW, SW]

def getpixel(img, x, y):
    width, height = img.size

    if x < 0:
        x=0
    elif x >= width:
        x = width-1

    if y < 0:
        y=0
    elif y >= height:
        y = height-1

    m = img.load()

    return m[x,y]

def filter(img, f):
    width, height = img.size
    imgdup = img.copy()
    flippedMatrix = imgdup.load()

    for x in range(width):
        for y in range(height):
            r = region3x3(img, x, y)
            flippedMatrix[x, y] = f(r)

    return imgdup