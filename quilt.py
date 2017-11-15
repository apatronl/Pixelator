#Alejandrina Patron Lopez
#GT ID 903075226
#apl7@gatech.edu
#Project 1

import numpy as np
import cv2
import random

#This function generates a quilt from an input image of size 400 x 400.
def quilt(inputIMG):
    w = inputIMG.shape[1]
    h = inputIMG.shape[0]
    pixels = 400
    sqrSize = 40

    #Crop image to 400 x 400 if not already that size.
    if (w > pixels) or (h > pixels) or (w < pixels) or (h < pixels):
        inputIMG = cropImage(inputIMG)

    outputIMG = inputIMG.copy()

    lowest = 0
    highestx = pixels - sqrSize
    highesty = pixels - sqrSize

    x1 = 0
    x2 = sqrSize
    y1 = 0
    y2 = sqrSize

    for y in range(pixels / sqrSize):
        for x in range(pixels / sqrSize):

            #Generate random x and y for patches such that (x + sqrSize < w) and (y + sqrSize < h).
            quiltX = random.randrange(lowest, highestx)
            quiltY = random.randrange(lowest, highesty)

            outputIMG[y1 : y2, x1 : x2] = inputIMG[quiltY : quiltY + sqrSize, quiltX : quiltX + sqrSize]

            x1 += sqrSize
            x2 += sqrSize
            if (x1 == pixels):
                x1 = 0
                x2 = sqrSize
                y1 += sqrSize
                y2 += sqrSize

    return outputIMG

#This function crops an image to size 400 x 400.
def cropImage(inputIMG):
    outputIMG = cv2.resize(inputIMG, (400, 400), interpolation = cv2.INTER_LINEAR)
    return outputIMG

#This function "pixelates" an input image of size 400 x 400.
def pixelate(inputIMG):
    w = inputIMG.shape[1]
    h = inputIMG.shape[0]
    pixels = 400
    size = 16

    #Crop image to 400 x 400 if not already that size.
    if (w > pixels) or (h > pixels) or (w < pixels) or (h < pixels):
        inputIMG = cropImage(inputIMG)

    outputIMG = inputIMG.copy()

    xstart = 0
    xend = 16
    ystart = 0
    yend = 16

    for y in range(pixels / size):
        for x in range(pixels / size):
            outputIMG[ystart : yend, xstart : xend, [0]] = getBlue(inputIMG[ystart + 7, xstart + 7])
            outputIMG[ystart : yend, xstart : xend, [1]] = getGreen(inputIMG[ystart + 7, xstart + 7])
            outputIMG[ystart : yend, xstart : xend, [2]] = getRed(inputIMG[ystart + 7, xstart + 7])
            xstart += size
            xend += size
            if (xstart == pixels):
                xstart = 0
                xend = size - 1
                ystart += size
                yend += size

    return outputIMG

#Returns blue value of a pixel.
def getBlue(point):
    return point[0]

#Returns green value of a pixel.
def getGreen(point):
    return point[1]

#Returns red value of a pixel.
def getRed(point):
    return point[2]

# a = cv2.imread("fruit.jpg")
# b = quilt(a)
# cv2.imwrite("quilt.jpg", b)
# c = pixelate(b)
# cv2.imwrite("pixels.jpg", c)
