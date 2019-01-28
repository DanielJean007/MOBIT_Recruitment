# Idea for this solution comes from: https://www.mathworks.com/help/images/correcting-nonuniform-illumination.html
# and https://codegolf.stackexchange.com/questions/40831/counting-grains-of-rice
import cv2
import numpy
import sys

img = cv2.imread('objetos.png',0)
h,w = img.shape

totalrice = 0
oldlinecount = 0
for y in range(0, h):
    oldc = 0
    linecount = 0
    start = 0   
    for x in range(0, w):
        c = img[y,x] < 128;
        if c == 1 and oldc == 0:
            start = x
        if c == 0 and oldc == 1 and (x - start) > 5:
            linecount += 1
        oldc = c
    if oldlinecount != linecount:
        if linecount < oldlinecount:
            totalrice += oldlinecount - linecount
        oldlinecount = linecount
print(totalrice)