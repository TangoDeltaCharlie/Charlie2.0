# This file holds all global variables to share across files

import queue

# TODO change this when connecting to IP for actual data transmission
TEST_MODE = True

# TODO this does nothing yet, might need to change for file pathing and xbox mapping
MAC_OSX = True

NO_XBOX = False



# Message Transfer Queues
receivingQueue = queue.Queue()
sendingQueue = queue.Queue()

#  Data From Pi
water_temp = 0.0
sub_temp = 0.0
buoy_temp = 0.0
sub_battery = 0.0
buoy_battery = 0.0
water_depth = 0.0
cargo_weight = 0.0

# laptop variables
xbox_a_pressed = False
xbox_b_pressed = False

low_power_mode_on = False

startProgram = False
quitProgram = False

program_running = False

pause_menu_is_up = False
buoyancy_calibration_menu_is_up = False
low_power_mode_screen_menu_is_up = False
high_temp_screen_menu_is_up = False

sub_temp_alert_has_been_displayed = False
buoy_temp_alert_has_been_displayed = False
sub_battery_at_30 = False
sub_battery_at_20 = False
sub_battery_at_10 = False
buoy_battery_at_30 = False
buoy_battery_at_20 = False
buoy_battery_at_10 = False


