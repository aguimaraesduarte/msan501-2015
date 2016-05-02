from filter import *

def median(data):
    return sorted(data)[len(data)/2]

img = open(sys.argv)
img.show()
img = filter(img, median) # denoise me please
img.show()