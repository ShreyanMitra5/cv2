import cv2 as cv
import numpy as np


#blank canvas, uint8 --> datatype of an image
#height, width, shape(color channels) --> (500, 500, 3)
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('blank', blank)

#1. Paint the image a certain color

#blank[row, column]
blank[200:300, 300:400] = 0, 255, 0
#cv.imshow('Green', blank)

#2. Draw a rectangle

#thickness = 2 indicates border thickness, putting cv.FILLED or -1    fills up the whole rectangle with that color
#to use fixed vals, we can do img.shape[1]//2 && img.shape[0]//2 for width & height respectively   
cv.rectangle(blank, (0, 0), (250, 250), (255, 0, 0), thickness=cv.FILLED)
#cv.imshow('Blank', blank)

#3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (0, 255, 0), thickness = 2)
cv.imshow('Circle', blank)

#4. How to draw a line
#same inputs as cv.rectangle(), just call using cv.line()

#5. Write text on an image
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX, fontScale=1.0, color=(0, 255, 0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)