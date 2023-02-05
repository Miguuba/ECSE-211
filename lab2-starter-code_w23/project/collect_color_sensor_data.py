#!/usr/bin/env python3

"""
This test is used to collect data from the color sensor.
It must be run on the robot.
"""

# Add your imports here, if any
from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor


COLOR_SENSOR_DATA_FILE = "../data_analysis/red_color_sensor.csv"

# complete this based on your hardware setup
COLOR_SENSOR = EV3ColorSensor(3)
TOUCH_SENSOR = TouchSensor(1)

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.


def collect_color_sensor_data():
    "Collect color sensor data."
    try:
        file1 = open(COLOR_SENSOR_DATA_FILE, "w")
        while True:
            if TOUCH_SENSOR.is_pressed():
                file1.write(str(COLOR_SENSOR.get_rgb()) + "\n")
                print(COLOR_SENSOR.get_rgb())
    except BaseException as exception:
        print(exception)
        exit()


if __name__ == "__main__":
    collect_color_sensor_data()
