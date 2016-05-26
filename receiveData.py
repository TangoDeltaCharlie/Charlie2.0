#Connect to IP, listen for new messages and put in Queue for dataProcessing to handle

import settings
import time


#TODO For testing have read file instead of connecting to IP
testing = True

def receiveData():

    if testing:
        # open file
        path = "testingFile.txt"
        inputs = open(path, "r")
    else:
        # connect to IP
        True

    while(True):

        if settings.quitProgram:
            inputs.close()
            print("Quitting receiveData Thread")
            break

        # read file line by line adding to queue
        if testing:
            message = inputs.readline()
            if message is None or message == '':
                inputs.close()
                inputs = open(path, "r")
            else:
                settings.receivingQueue.put(message)
            time.sleep(1)
        else:
            # TODO get messages over wifi
            # Add to queue like above in test mode
            pass