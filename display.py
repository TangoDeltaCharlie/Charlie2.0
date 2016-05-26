import numpy as np
import cv2

import settings
import time

def displayGUI():

    height = 480
    width = 640
    startImage = np.zeros((height,width,3), np.uint8)
    text_color = (255, 0, 0)
    cv2.putText(startImage, "Loading Screen...", (10, 50), cv2.FONT_HERSHEY_TRIPLEX, 1.0, text_color)
    cv2.imshow('Charlie 2.0', startImage)

    print("In GUI Loop")
    while(True):
        if settings.quitProgram:
            break

        cv2.imshow('Charlie 2.0', startImage)
        #wait for A to be pressed or B to Quit

        #if cv2.waitKey(1) & 0xFF == ord('a'):
        #    settings.startProgram = True
        #    break
        #elif cv2.waitKey(1) & 0xFF == ord('b'):
        #    settings.quitProgram = True
        #    break

        time.sleep(0.01)


    if settings.startProgram:
        #TODO Change to Webcam
        cap = cv2.VideoCapture(0)

        while(True):
            if settings.quitProgram:
                break

            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            #TODO Draw all text and background images

            x = np.size(frame, 1)
            y = np.size(frame, 0)
            text_color = (255, 0, 0)
            cv2.putText(gray, "Sensor Status: DOWN", (10, 50), cv2.FONT_HERSHEY_TRIPLEX, 1.0, text_color)

            #TODO Draw popups here

            #gray = cv2.resize(gray, (0,0), fx=2, fy=2)

            # Display the resulting frame
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                settings.quitProgram = True
                break

        # When everything done, release the capture
        cap.release()

    cv2.destroyAllWindows()


