import cv2
import datetime
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# USing set method use camera width height
cap.set(3,600)
cap.set(4,600)
print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: '+str(cap.get(3)) +' Height: '+str(cap.get(4))
        dateTim = str(datetime.datetime.now())
        frame = cv2.putText(frame,dateTim, (10,50), font, 1, (0,255,255), 2, cv2.LINE_AA)

        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
