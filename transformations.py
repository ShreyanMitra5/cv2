import cv2 as cv
import numpy as np


img = cv.imread('/Users/shreyanmitra/Desktop/Coding_Projects/opencv/Resources/Photos/park.jpg')

#Translation
def translation(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return(cv.warpAffine(img, transMat, dimensions))

# -x --> Left
# x --> Right
# -y --> Up
# y --> Down

new_img = translation(img, 100, 40)
cv.imshow('Translated image', new_img)

#Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    #Third parameter is scaling the img
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return(cv.warpAffine(img, rotMat, dimensions))

#Second parameter is the degree amount you want rotated || >0 is cc, <0 is clockwise
rotatedImage = rotate(img, -40)
cv.imshow('rotated img', rotatedImage)

rotate_rotated = rotate(rotatedImage, -40)
cv.imshow('Rotated of rotated img', rotate_rotated)

#Flipping
#2nd parameter is only 3 vals --> 0: Vertical Flip, 1: Hor. Flip, -1: Hor && Vert
flip = cv.flip(img, 0)
cv.imshow('flipped img', flip)
cv.waitKey(0)

#Cropping & resize are in rescale.py