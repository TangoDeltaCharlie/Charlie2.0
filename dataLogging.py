# This file logs all sensor data in a file
import settings
import time
import datetime

# Number of seconds between log
LOG_INTERVAL = 1


def log_data():

    high_sub_temp_has_been_alerted = False
    high_buoy_temp_has_been_alerted = False

    datetime_string = datetime.datetime.now().strftime("%m%d%Y-%H%M%S")

    # TODO Change file path per user
    path = "/Users/Scott/Desktop/Charlie2.0/DataLogs/" + datetime_string + "Log.txt"

    log_file = open(path, 'w+')

    log_file.write("%15s%15s%15s%15s%15s%15s%15s\n" %
                   ("TIME", "USS BATTERY", "BUOY BATTERY", "USS TEMP", "BUOY TEMP", "WATER TEMP", "WATER DEPTH"))

    while True:

        if settings.quitProgram:
            log_file.close()
            print("Quitting dataLogging Thread")
            break

        time_string = datetime.datetime.now().strftime("%H:%M:%S")

        log_file.write("%15s" % time_string)
        log_file.write("%15s" % str(settings.sub_battery))
        log_file.write("%15s" % str(settings.buoy_battery))
        log_file.write("%15s" % str(settings.sub_temp))
        log_file.write("%15s" % str(settings.buoy_temp))
        log_file.write("%15s" % str(settings.water_temp))
        log_file.write("%15s\n" % str(settings.water_depth))

        # High USS Temp
        if settings.sub_temp_alert_has_been_displayed and not high_sub_temp_has_been_alerted:
            log_file.write("%15s %s\n" % (time_string, "ALERT: USS Temperature Has Reached A Critical Temperature"))
            high_sub_temp_has_been_alerted = True

        elif settings.sub_temp_alert_has_been_displayed and high_sub_temp_has_been_alerted:
            pass

        elif not settings.sub_temp_alert_has_been_displayed:
            high_sub_temp_has_been_alerted = False

        # High Buoy Temp
        if settings.buoy_temp_alert_has_been_displayed and not high_buoy_temp_has_been_alerted:
            log_file.write("%15s %s\n" % (time_string, "ALERT: BUOY Temperature Has Reached A Critical Temperature"))
            high_buoy_temp_has_been_alerted = True

        elif settings.buoy_temp_alert_has_been_displayed and high_buoy_temp_has_been_alerted:
            pass

        elif not settings.buoy_temp_alert_has_been_displayed:
            high_buoy_temp_has_been_alerted = False

        time.sleep(1)

