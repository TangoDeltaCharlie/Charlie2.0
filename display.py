import cv2
import numpy as np

import settings

cap = None


def display_launch_screen():
    width = 720
    height = 480

    start_image = np.zeros((height, width, 3), np.uint8)

    # TODO Draw A Welcome Screen
    thickness = 1
    font_face = cv2.FONT_HERSHEY_SIMPLEX

    text_color = (255, 0, 0)
    scale = 1
    text_size = cv2.getTextSize("Welcome to Charlie2.0", font_face, scale, thickness)
    width_start = (width - text_size[0][0])/2
    cv2.putText(start_image, "Welcome to Charlie2.0", (int(round(width_start)), 100), font_face, scale, text_color,
                thickness)

    text_color = (0, 255, 0)
    scale = .75
    text_size = cv2.getTextSize("Press A to Start", font_face, scale, thickness)
    width_start = (width - text_size[0][0])/2
    cv2.putText(start_image, "Press A to Start", (int(round(width_start)), 250), font_face, scale, text_color,
                thickness)

    text_color = (0, 0, 255)
    scale = .75
    text_size = cv2.getTextSize("Press B to Quit", font_face, scale, thickness)
    width_start = (width - text_size[0][0])/2
    cv2.putText(start_image, "Press B to Quit", (int(round(width_start)), 300), font_face, scale, text_color,
                thickness)

    cv2.imshow('Charlie 2.0', start_image)

    # Wait for A to be pressed to Launch or B to Quit
    while True:
        if settings.xbox_a_pressed:
            settings.xbox_a_pressed = False
            settings.startProgram = True
            break
        elif settings.xbox_b_pressed:
            settings.xbox_b_pressed = False
            settings.quitProgram = True
            break

        # TODO Remove this once only using XBOX
        if cv2.waitKey(1) & 0xFF == ord('A'):
            settings.startProgram = True
            break
        elif cv2.waitKey(1) & 0xFF == ord('B'):
            settings.quitProgram = True
            break


def display_live_feed():
    global cap

    # TODO Connect to Video Camera
    #cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        #ret, frame = cap.read()

        # TODO Draw popups here
        #if settings.pause_menu_is_up:
            #frame = display_pause_menu(frame)

        #elif settings.buoyancy_calibration_menu_is_up:
            #frame = display_buoyancy_calibration_menu(frame)

        #elif settings.low_power_mode_screen_menu_is_up:
            #frame = display_low_power_menu(frame)

        #elif settings.high_temp_screen_menu_is_up:
            #frame = display_high_temp_menu(frame)



        # gray = cv2.resize(gray, (0,0), fx=2, fy=2)

        # Display the resulting frame
        height = 100
        width = 200
        frame = np.zeros((height,width,3), np.uint8)

        frame = display_data(frame)

        cv2.imshow('Charlie 2.0', frame)

        if cv2.waitKey(1) & 0xFF == ord('Q'):
            settings.quitProgram = True
            break


def display_data(frame):

    overlay = frame.copy()

    light_gray = (144, 128, 112)
    cv2.rectangle(overlay, (0, 0), (200, 100), light_gray, -1)

    opacity = 0.6
    cv2.addWeighted(overlay, opacity, frame, 1 - opacity, 0, frame)

    # TODO Draw all text and background images
    # x = np.size(frame, 1)-50
    # y = np.size(frame, 0)-50
    x = 2
    y = 15
    text_color = (255, 0, 0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = .5
    line_type = cv2.LINE_AA
    thickness = 1



    cv2.putText(frame, "Water Depth:  " + str(settings.water_depth), (x, y), font, font_scale, text_color,
                thickness, line_type)
    y = y + 15

    cv2.putText(frame, "Water Temp:   " + str(settings.water_temp), (x, y), font, font_scale, text_color,
                thickness, line_type)
    y = y + 15

    text_color = set_text_color_temp(settings.sub_temp)
    cv2.putText(frame, "Sub Temp:     " + str(settings.sub_temp), (x, y), font, font_scale, text_color,
                thickness, line_type)
    y = y + 15

    text_color = set_text_color_temp(settings.buoy_temp)
    cv2.putText(frame, "Buoy Temp:    " + str(settings.buoy_temp), (x, y), font, font_scale, text_color,
                thickness, line_type)
    y = y + 15

    text_color = set_text_color_battery(settings.sub_battery)
    cv2.putText(frame, "Sub Battery:   " + str(settings.sub_battery), (x, y), font, font_scale, text_color,
                thickness, line_type)
    y = y + 15

    text_color = set_text_color_battery(settings.buoy_battery)
    cv2.putText(frame, "Buoy Battery:  " + str(settings.buoy_battery), (x, y), font, font_scale, text_color,
                thickness, line_type)


    return frame

def set_text_color_temp(temp):
    red    = (0, 0, 255)
    yellow = (0, 255, 255)
    blue   = (255, 0, 0)

    if temp >= 90.0:
        return red
    elif temp >= 70.0:
        return yellow
    else:
        return blue

def set_text_color_battery(battery):
    red    = (0, 0, 255)
    yellow = (0, 255, 255)
    blue   = (255, 0, 0)

    if battery <= 10.0:
        return red
    elif battery <= 20.0:
        return yellow
    else:
        return blue


def display_pause_menu(frame):

    menu_title = "Pause Menu"
    frame = draw_pop_up_background(frame)
    frame = draw_menu_title(frame, menu_title)

    font = cv2.FONT_HERSHEY_SIMPLEX
    line_type = cv2.LINE_AA
    text_color = (255, 255, 255)
    font_scale = .5
    thickness = 1

    text_size = cv2.getTextSize("Press B to Cancel", font, font_scale, thickness)
    width_start = (np.size(frame, 1) - text_size[0][0]) / 2
    cv2.putText(frame, "Press B to Cancel", (int(round(width_start)), int(round(np.size(frame, 0) / 2))), font,
                font_scale, text_color, thickness, line_type)

    return frame


def display_buoyancy_calibration_menu(frame):
    menu_title = "Buoyancy Calibration"
    frame = draw_pop_up_background(frame)
    frame = draw_menu_title(frame, menu_title)

    return frame


def display_low_power_menu(frame):
    menu_title = "Low Power Mode - Battery"
    frame = draw_pop_up_background(frame)
    frame = draw_menu_title(frame, menu_title)

    return frame


def display_high_temp_menu(frame):
    menu_title = "Low Power Mode - Critical Temp"
    frame = draw_pop_up_background(frame)
    frame = draw_menu_title(frame, menu_title)

    return frame


def draw_menu_title(frame, menu_title):

    font = cv2.FONT_HERSHEY_SIMPLEX
    line_type = cv2.LINE_AA
    text_color = (255, 255, 255)
    font_scale = .5
    thickness = 1

    text_size = cv2.getTextSize(menu_title, font, font_scale, thickness)
    width_start = (np.size(frame, 1) - text_size[0][0]) / 2
    cv2.putText(frame, menu_title, (int(round(width_start)), int(round(np.size(frame, 0)/2))-50), font, font_scale,
                text_color, thickness, line_type)

    return frame


def draw_pop_up_background(frame):
    overlay = frame.copy()
    height = int(round(np.size(frame, 0)/2))
    width = int(round(np.size(frame, 1)/2))
    light_gray = (144, 128, 112)
    cv2.rectangle(overlay, (width-150, height-75), (width+150, height+75), light_gray, -1)

    opacity = 0.6
    cv2.addWeighted(overlay, opacity, frame, 1 - opacity, 0, frame)

    return frame


def close():
    global cap
    print("Quitting Display")
    if cap is not None:
        cap.release()
    cv2.destroyAllWindows()
