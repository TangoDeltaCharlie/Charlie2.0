# This file sends data to the pi

import settings
import time

def send_data():

    if not settings.TEST_MODE:
        # Connect to IP
        pass

    while True:

        if settings.quitProgram:
            if not settings.TEST_MODE:
                # TODO disconnect from IP
                pass

            print("Quitting sendData Thread")
            break

        if settings.TEST_MODE:

            try:
                message = settings.sendingQueue.get(False, None)
                print("Sending Message = " + message)

                # TODO REMOVE SLEEP
                time.sleep(1)
            except settings.queue.Empty:
                print("Sending Queue is Empty")
                time.sleep(1)

        else:
            # TODO send over IP
            pass

