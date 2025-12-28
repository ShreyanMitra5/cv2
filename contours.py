import cv2 as cv
import numpy as np 

img = cv.imread('/Users/shreyanmitra/Desktop/Coding_Projects/opencv/Resources/Photos/cats 2.jpg')

blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

#Different from converting to grayscale. Grayscale converts to many shades of gray, while 
# threshold just binarizes into either white or black
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('threshed img', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)

