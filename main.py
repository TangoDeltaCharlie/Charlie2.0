#This is the main function for charlie 2.0

import settings
import dataProcessing
import receiveData
import xboxController

import sys
import threading
import cv2
import numpy as np

cap = None
thread1 = None
thread2 = None


def main():

    global thread1
    global thread2

    try:

        xboxCont = xboxController.XboxController(None, deadzone=30, scale=100, invertYAxis=True)
        xboxCont.start()
        displayLaunchScreen()

        # Wait for A to be pressed to Launch or B to Quit
        while (True):
            if settings.xbox_a_pressed:
                settings.xbox_a_pressed = False
                settings.startProgram = True
                break
            elif settings.xbox_b_pressed:
                settings.xbox_b_pressed = False
                settings.quitProgram = True
                break

            #TODO Remove this once only using XBOX
            if cv2.waitKey(1) & 0xFF == ord('A'):
                settings.startProgram = True
                break
            elif cv2.waitKey(1) & 0xFF == ord('B'):
                settings.quitProgram = True
                break

        if settings.startProgram:
            # Start all Threads here
            thread1 = threading.Thread(target=receiveData.receiveData, args=())
            thread1.start()
            thread2 = threading.Thread(target=dataProcessing.processData, args=())
            thread2.start()

            displayLiveFeed()

            quitProgram()
        else:
            cv2.destroyAllWindows()

    except (KeyboardInterrupt, SystemExit):
        quitProgram()
        sys.exit()


def displayLaunchScreen():
    height = 480
    width = 640
    start_image = np.zeros((height, width, 3), np.uint8)
    text_color = (255, 0, 0)

    # TODO Draw A Welcome Screen
    cv2.putText(start_image, "Press A to Start", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, .75, text_color)
    cv2.putText(start_image, "Press B to Quit", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, .75, text_color)
    cv2.imshow('Charlie 2.0', start_image)


def displayLiveFeed():
    global cap

    # TODO Connect to Video Camera
    cap = cv2.VideoCapture(0)

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # TODO Draw all text and background images
        # x = np.size(frame, 1)-50
        # y = np.size(frame, 0)-50
        x = 2
        y = 15
        text_color = (255, 255, 255)
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = .5
        cv2.putText(frame, "Water Temp:   " + str(settings.waterTemp), (x, y), font, fontScale, text_color, 1, cv2.LINE_AA)
        y = y + 15
        cv2.putText(frame, "Sub Temp:     " + str(settings.subTemp), (x, y), font, fontScale, text_color, 1, cv2.LINE_AA)
        y = y + 15
        cv2.putText(frame, "Buoy Temp:    " + str(settings.buoyTemp), (x, y), font, fontScale, text_color, 1, cv2.LINE_AA)
        y = y + 15
        cv2.putText(frame, "Sub Battery:   " + str(settings.subBattery), (x, y), font, fontScale, text_color, 1, cv2.LINE_AA)
        y = y + 15
        cv2.putText(frame, "Buoy Battery:  " + str(settings.buoyBattery), (x, y), font, fontScale, text_color, 1, cv2.LINE_AA)

        # TODO Draw popups here

        # gray = cv2.resize(gray, (0,0), fx=2, fy=2)

        # Display the resulting frame
        cv2.imshow('Charlie 2.0', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            settings.quitProgram = True
            break


def quitProgram():
    global cap

    print("Quitting Main")
    settings.quitProgram = True
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

