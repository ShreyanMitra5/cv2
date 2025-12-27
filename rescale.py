import cv2 as cv

img = cv.imread('/Users/shreyanmitra/Desktop/Coding_Projects/opencv/Resources/Photos/cats 2.jpg')

cv.imshow('Cat', img)

#rescales image/video frame by frame || the scale is 0.7
def rescaleFrame(frame, scale=0.7):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    #Interpolation declares the algorithm in which the open-cv converts the image
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#func to rescale LIVE videos solely, and not images || doesn't work with premade vids either
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture('/Users/shreyanmitra/Desktop/Coding_Projects/opencv/Resources/Videos/dog.mp4')

resized_image = rescaleFrame(img)
cv.imshow('Resized Cat', resized_image)

while True:
    #loads frame by frame
    isTrue, frame = capture.read()

    frame_resize = rescaleFrame(frame, 0.75)

    #cv.imshow('Video', frame)
    #cv.imshow('Video Resized', frame_resize)

    #displays each frame
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

#stops running software & closes all windows
capture.release()
cv.destroyAllWindows()


