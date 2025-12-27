import cv2 as cv

#converts image into arrays of pixels
#img = cv.imread('/Users/shreyanmitra/Desktop/Coding_Projects/opencv/Resources/Photos/cat.jpg')

#display image
#cv.imshow('Cat', img)

#reading videos
capture = cv.VideoCapture('/Users/shreyanmitra/Desktop/Coding_Projects/opencv/Resources/Videos/dog.mp4')

while True:
    #loads frame by frame
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    #displays each frame
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

#stops running software & closes all windows
capture.release()
cv.destroyAllWindows()

#If input is 0, then enter any key to exit. If >0 then the comp will show the img for that many milisecond
#cv.waitKey(0)