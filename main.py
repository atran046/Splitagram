import sys
import os
from PIL import Image
from math import floor
# import re

# the following regex works for extracting basic filename.jpg
# result = re.match(r'.*[^.jpg]', sys.argv[1]) 

def splitImage(numParts):
    for x in range(numParts):
        region = (getX(x, im.width, numParts), 0, getX(x+1, im.width, numParts), im.height)
        section = im.crop(region)

        file = ''.join([str(fileName), '/', str(fileName), '-', str(x), '.jpg'])
        section.save(file)

def getX(section, width, numParts):
    return section * floor(width/numParts)

def splitForInsta(width, height):
    math.ceil(width/height)
    
#TODO: Make sure that file exists
fileName = sys.argv[1].split('.')[0]

#Save sections to directory
if(os.path.exists(str(fileName)) == False):
    os.mkdir(str(fileName))

im = Image.open(sys.argv[1])
splitImage(int(sys.argv[2]))