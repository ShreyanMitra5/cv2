import cv2 as cv

img = cv.imread('/Users/shreyanmitra/Desktop/Coding_Projects/opencv/Resources/Photos/cats.jpg')

cv.imshow('Cat', img)


#1. Convert image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#cv.imshow('Grayscaled Img', gray)

#2. Blur
#Second parameter is the gausian kernel you want to blur, 
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)

#cv.imshow('Blurred Img', blur)


#3. Edge cascasde

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Image', canny)

#4. Dilate image

dilated = cv.dilate(canny, (3, 3), iterations=3)

cv.imshow('Dilated image', dilated)

#5. Eroded
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('eroded img', eroded)

#6. Resize an img

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#7. Crop an image
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)
cv.waitKey(0)
 