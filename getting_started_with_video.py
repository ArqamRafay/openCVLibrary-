# https://www.youtube.com/watch?v=-RtVZsCvXAQ
import cv2

cap = cv2.VideoCapture(0)


# while loop use for frame continue

while(True):
    ret, frame = cap.read()

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('frame', gray)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Releaswe the caputer variable
cap.release()
cv2.destroyAllWindows()
