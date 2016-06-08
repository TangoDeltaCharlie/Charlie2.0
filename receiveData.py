# Connect to IP, listen for new messages and put in Queue for dataProcessing to handle

import settings
import time


# TODO For testing have read file instead of connecting to IP


def receive_data():

    if settings.TEST_MODE:
        # open file
        path = "testingFile.txt"
        inputs = open(path, "r")

    else:
        # connect to IP
        True

    while True:

        if settings.quitProgram:
            if settings.TEST_MODE:
                inputs.close()

            else:
                # TODO disconnet from IP
                pass

            print("Quitting receiveData Thread")
            break

        # read file line by line adding to queue
        if settings.TEST_MODE:
            message = inputs.readline()

            if message is None or message == '':
                inputs.close()
                inputs = open(path, "r")

            else:
                settings.receivingQueue.put(message)
            time.sleep(1)

        else:
            # TODO get messages over wifi
            # TODO check if still connected
            # Add to queue like above in test mode
            # settings.receivingQueue.put(message)
            pass