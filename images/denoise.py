import sys
from PIL import Image

def denoise(img):
    width, height = img.size
    imgdup = img.copy()
    flippedMatrix = imgdup.load()

    for x in range(width):
        for y in range(height):
            r = region3x3(img, x, y)
            flippedMatrix[x, y] = median(r)

    return imgdup

def median(data):
    return sorted(data)[len(data)/2]

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
    return [me, N, NE, E, SE, S, SW, W, NW]

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

if len(sys.argv)<=1:
    print "missing image filename"
    sys.exit(1)

filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()

imgdup = denoise(img)
imgdup.show()