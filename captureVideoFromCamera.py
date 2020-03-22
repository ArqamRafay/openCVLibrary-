# https://www.youtube.com/watch?v=-RtVZsCvXAQ
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# forcc = cv2.VideoWriter_forcc(*'XVID')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
framPerSecond = 20
 
 # Define the codec and create VideoWriter object
out = cv2.VideoWriter('output.mp4', fourcc, framPerSecond, (640,480))

print(cap.isOpened())

# while loop use for frame continue
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    if ret == True:
        
        # getting frame width and height
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
 
        out.write(frame)
        # Display the resulting frame
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('frame', gray)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
