import cv2
import numpy as np
import datetime

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#cap.set(3,1280)
#cap.set(4, 720)

#print(cap.get(3))
#print(cap.get(4))

fourcc = cv2.VideoWriter_fourcc(*'XVID')

#save = cv2.VideoWriter('save.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret==True:

        font = cv2.FONT_HERSHEY_TRIPLEX
        #text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4)) 
        date = str(datetime.datetime.now())
        
        #save.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.putText(frame, date, (10,50), font, 1, (201,91,189), 2, cv2.LINE_AA)  
        frame = cv2.rectangle(frame, (0,10), (520,60), (181,109,54), 10) 
        gray = cv2.putText(gray, date, (10,50), font, 1, (201,91,189), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        cv2.imshow('gray', gray)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
