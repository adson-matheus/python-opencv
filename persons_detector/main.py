import cv2 as cv
import numpy as np

def main():
    personsDetector('people.mp4')
    #personsDetector(0+cv.CAP_DSHOW) #abre a propria camera

def personsDetector(link):
    cap = cv.VideoCapture(link)

    #funcao que remove o background
    removeBackground = cv.createBackgroundSubtractorMOG2(history=100, varThreshold=40, detectShadows=False)

    while True:
        ret, frame = cap.read()
        if frame is None:
            break
        if ret:
            #aplica a remocao de background em cada frame
            mask = removeBackground.apply(frame)
            
            #pega apenas o branco, ignora o restante
            _, mask = cv.threshold(mask, 254, 255, cv.THRESH_BINARY)
            contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                area = cv.contourArea(cnt)
                if area > 150:
                    x, y, w, h = cv.boundingRect(cnt)
                    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            cv.imshow('Contador de Pessoas', frame)
            cv.imshow('Mask', mask)

            #esc sai
            if cv.waitKey(30) == 27:
                break
        else:
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()