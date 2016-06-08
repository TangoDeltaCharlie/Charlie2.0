# This file handles data after its received from the Pi
# Analyze data and disaply on GUI

import settings
import time


def process_data():

    while True:

        if settings.quitProgram:
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


# FIELDS
# WaterTemp
# SubTemp
# BouyTemp
# SubBattery
# BouyBattery
# Depth

# messages come in format of WATERTEMP:80
def handleMessage(message):

    messageList = message.split(':')

    key = messageList[0]
    value = messageList[1]
    # Strip New Line Char
    value = value.rstrip()

    value = float(value)

    if key == 'WATERTEMP':
        settings.water_temp = value

    elif key == "SUBTEMP":
        settings.sub_temp = value
        if value > 90.0 and not settings.sub_temp_alert_has_been_displayed:
            settings.sub_temp_alert_has_been_dispalyed = True
            settings.low_power_mode_screen_menu_is_up = True
        else:
            settings.sub_temp_alert_has_been_dispalyed = False

    elif key == "BUOYTEMP":
        settings.buoy_temp = value
        if value > 90.0 and not settings.buoy_temp_alert_has_been_displayed:
            settings.buoy_temp_alert_has_been_displayed = True
            settings.low_power_mode_screen_menu_is_up = True
        else:
            settings.buoy_temp_alert_has_been_displayed = False

    elif key == "SUBBATTERY":
        settings.sub_battery = value
        if value < 30.0 and not settings.sub_battery_at_30:
            settings.sub_battery_at_30 = True
            settings.sub_temp_alert_has_been_displayed = True

        elif value < 20.0 and not settings.sub_battery_at_20:
            settings.sub_battery_at_20 = True
            settings.sub_temp_alert_has_been_displayed = True

        elif value < 10.0 and not settings.sub_battery_at_10:
            settings.sub_battery_at_10 = True
            settings.sub_temp_alert_has_been_displayed = True

    elif key == "BUOYBATTERY":
        settings.buoy_battery = value
        if value < 30.0 and not settings.buoy_battery_at_30:
            settings.buoy_battery_at_30 = True
            settings.buoy_temp_alert_has_been_displayed = True

        elif value < 20.0 and not settings.buoy_battery_at_20:
            settings.buoy_battery_at_20 = True
            settings.buoy_temp_alert_has_been_displayed = True

        elif value < 10.0 and not settings.buoy_battery_at_10:
            settings.buoy_battery_at_10 = True
            settings.buoy_temp_alert_has_been_displayed = True

    elif key == "DEPTH":
        settings.water_depth = value
