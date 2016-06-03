#This file handles data after its received from the Pi
#Logs and sends it to display for display via global variable

import settings
import time
import datetime

log_file = None

def processData():

    global log_file

    datetimeString = datetime.datetime.now().strftime("%m%d%Y-%H%M%S")
    #TODO Change file path per user
    path = "/Users/Scott/Desktop/Charlie/DataLogs/" + datetimeString + "Log.txt"

    log_file = open(path, 'w+')

    i = 0

    while (True):

        if settings.quitProgram:
            log_file.close()
            print("Quitting dataProcessing Thread")
            break

        try:
            message = settings.receivingQueue.get(False, None)
            print("Receiving Message = " + message)
            if message != '' and message is not None:
                handleMessage(message)

            #TODO REMOVE SLEEP
            time.sleep(1)
        except settings.queue.Empty:
            print("Receiving Queue is Empty")
            time.sleep(1)


#TODO FIELDS
#WaterTemp
#SubTemp
#BouyTemp
#SubBattery
#BouyBattery

#messages come in format of WATERTEMP:80
def handleMessage(message):

    messageList = message.split(':')

    key = messageList[0]
    value = messageList[1]
    # Strip New Line Char
    value = value.rstrip()

    timeString = datetime.datetime.now().strftime("%H:%M:%S")

    #TODO file logging into columns with set widths, might put in seperate thread and print all values every second
    log_file.write(timeString + " " + key + " " + value + "\n")

    #TODO add extreme temp or low battery level processing

    if key == 'WATERTEMP':
        settings.water_temp = value
    elif key == "SUBTEMP":
        settings.sub_temp = value
    elif key == "BUOYTEMP":
        settings.buoy_temp = value
    elif key == "SUBBATTERY":
        settings.sub_battery = value
    elif key == "BUOYBATTERY":
        settings.buoy_battery = value
