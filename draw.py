import cv2
import numpy as np

#img = cv2.imread('lena.jpg',1)

img = np.zeros([512,512,3], np.uint8)

height, width, channels = img.shape 
print(img.shape)

font = cv2.FONT_HERSHEY_DUPLEX

img = cv2.line(img, (0,0), (100,100), (0,0,150), 3)
img = cv2.arrowedLine(img, (150,150), (150,200), (0,150,0), 3)
img = cv2.rectangle(img, (200,200), (300,300), (200,0,0), -1)
img = cv2.circle(img, (400,400), 50, (200,0,230), 5)
img = cv2.putText(img, 'sea', (200,250), font, 2, (200,100,500), 2, cv2.LINE_4)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
