import cv2
print(cv2.__version__)

# second param tell color ,gray scale etc
img = cv2.imread('car.jpg', -1)
# print(img)

cv2.imshow('image', img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('car123.jpg', img)
    cv2.destroyAllWindows()

# duplicate of image
# cv2.imwrite('car123.jpg', img)
