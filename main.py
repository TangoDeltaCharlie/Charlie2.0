# This is the main function for charlie2.0

import settings
import dataProcessing
import receiveData
import xboxController
import display
import sendData
import dataLogging

import sys
import threading


def main():

    try:

        #if not settings.NO_XBOX:
        #    xbox_controller_thread = xboxController.XboxController(None, deadzone=30, scale=100, invertYAxis=True)
        #   xbox_controller_thread.start()

        display.display_launch_screen()

        if settings.startProgram:
            settings.program_running = True

            # Start all Threads here
            thread1 = threading.Thread(target=receiveData.receive_data, args=())
            thread1.start()
            thread2 = threading.Thread(target=dataProcessing.process_data, args=())
            thread2.start()
            #thread3 = threading.Thread(target=sendData.send_data, args=())
            #thread3.start()
            thread4 = threading.Thread(target=dataLogging.log_data, args=())
            thread4.start()

            display.display_live_feed()

            quit_program()

        else:
            quit_program()

    except (KeyboardInterrupt, SystemExit):
        quit_program()


def quit_program():

    settings.quitProgram = True

    display.close()

    print("Quitting Main")
    sys.exit()


if __name__ == "__main__":
    main()

