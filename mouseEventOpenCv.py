import numpy as np
import cv2

# Event available in cv2 
# events = [i for i in dir(cv2) if 'EVENT' in  i]
# print(events)

# click event to get co-oridnate
def click_event(event, x,y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ' , '+ str(y)
        cv2.putText(img, strXY, (x,y), font, 0.5, (255,255,0), 2)
        cv2.imshow('image', img)
    # showing rgb color picker
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]   # get blue channel from this image
        green = img[y,x,1]  # get green channel from this image
        red = img[y,x,2]  
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ' , '+ str(green) + ' , '+ str(red)
        cv2.putText(img, strBGR, (x,y), font, 0.5, (0,255,255), 2)
        cv2.imshow('image', img)   

# click event to get color and reopen new windows
def click_eventReopenWindowsWithColor(event, x,y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]   # get blue channel from this image
        green = img[y,x,1]  # get green channel from this image
        red = img[y,x,2]  
        cv2.circle(img, (x,y),3, (0,0,255), -1)
        mycolorimage = np.zeros((512,512,3), np.uint8)
        mycolorimage[:] = [blue, green, red]
        cv2.imshow('colorWindow', mycolorimage)


# Create black image using np
# img = np.zeros((512,512,3),np.uint8)
# colord img, 
img = cv2.imread('car.jpg')
cv2.imshow('image', img)
points = []
#  method call
cv2.setMouseCallback('image', click_event)
# cv2.setMouseCallback('image', click_eventReopenWindowsWithColor)

cv2.waitKey(0)
cv2.destroyAllWindows()
