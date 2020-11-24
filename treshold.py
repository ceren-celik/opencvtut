import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while (True):
    (ret, frame) = cap.read()
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteFrame) = cv.threshold(grayFrame, 127, 255, cv.THRESH_BINARY)

    img = cv.imread('gradient.png', 0)
    _, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    _, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
    _, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
    _, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)

    cv.imshow("Image", img)
    cv.imshow("th1", th1)
    cv.imshow("th2", th2) 
    cv.imshow("th3", th3)
    cv.imshow("th4", th4)
    cv.imshow("blackAndWhiteFrame", blackAndWhiteFrame)
    cv.imshow("frame", frame)

    if cv.waitKey(1) == 27:
        break

cap.release()
cv.waitKey(0)
cv.destroyAllWindows()