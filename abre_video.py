import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0+cv.CAP_DSHOW)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Exiting ...")
        break

    # Display the resulting frame
    cv.imshow('Sorria', frame)
    if cv.waitKey(1) == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
