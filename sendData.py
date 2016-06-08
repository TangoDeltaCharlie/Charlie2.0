# This file sends data to the pi

import settings
import time


def send_data():

    if not settings.TEST_MODE:
        # TODO Connect to IP
        pass

    while True:

        if settings.quitProgram:
            if not settings.TEST_MODE:
                # TODO disconnect from IP
                pass

            print("Quitting sendData Thread")
            break

        try:
            message = settings.sendingQueue.get(False, None)

            if message != '' and message is not None:

                if settings.low_power_mode_on:
                    # Cut thrust in half for low power mode
                    messageList = message.split(':')

                    key = messageList[0]
                    value = messageList[1]
                    value = float(value)
                    value = value/2
                    value = str(value)
                    message = key + ":" + value

                if settings.TEST_MODE:
                    try:
                        print("Sending Message = " + message)

                        # TODO REMOVE SLEEP
                        # time.sleep(1)
                    except settings.queue.Empty:
                        print("Sending Queue is Empty")
                        # TODO REMOVE SLEEP
                        time.sleep(1)

                else:
                    # TODO send over IP
                    # TODO check if still connected
                    pass

        except settings.queue.Empty:
            pass

