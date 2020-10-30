import cv2
import numpy as np

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

save = cv2.VideoWriter('save.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret==True:

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        save.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        cv2.imshow('frame', frame)
        cv2.imshow('gray', gray)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()