import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0+cv.CAP_DSHOW)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('saida_do_video.avi', fourcc, 10.0, (640,  480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv.flip(frame, 180)

    # write the flipped frame
    out.write(frame)
    cv.imshow('frame', frame)

    if cv.waitKey(2) == ord('q'):
        break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()