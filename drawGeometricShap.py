import numpy as np
import cv2

img = cv2.imread('car.jpg', 1)

img = cv2.line(img, (0,0), (255,255), (147,96,44), 5)
img = cv2.arrowedLine(img, (0,255), (255,255), (255,0,0), 5)
img = cv2.rectangle(img , (10,10), (100,100), (0,0,255),5)
img = cv2.circle(img,(447,63),63, (0,0,255), 2)
# -1 indecate the fill color of circle
# img = cv2.circle(img,(447,63),63, (0,0,255), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Open Cv ', (10,500), font,4, (255,255,255),10, cv2.LINE_AA)

cv2.imshow('imag',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
