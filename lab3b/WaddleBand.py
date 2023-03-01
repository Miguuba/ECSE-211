#!/usr/bin/python3
 
from utils.sound import Sound, Song
from utils.brick import TouchSensor, Motor, BP
import time
import math

# ----------- BUTTONS -------------
TS_S1 = TouchSensor(1)
TS_S2 = TouchSensor(2)
TS_S3 = TouchSensor(3)
TS_S4 = TouchSensor(4) # Emergency stop

STATE = 0 # default status = 0, no button is pressed
DEBOUNCING_INTERVAL = 0.5 # in seconds

def emergency_isPressed() -> bool:
    pass

def combo_state():
    combo = [int(TS_S1.is_pressed()), int(TS_S2.is_pressed()), int(TS_S3.is_pressed())]
    if combo == [1,0,0]: # play note 1
        return 1
    elif combo == [0,1,0]: # play note 2
        return 2
    elif combo == [0,0,1]: # play note 3
        return 3
    elif combo == [1,1,0]: # play note 4
        return 4
    elif combo == [0,1,1]: # play note 5
        return 5
    elif combo == [1,0,1]: # play note 6 ! I think this should be the drum combo
        return 6
    elif combo == [1,1,1]: # play DRUM!
        return 7
    return 0

# ----------- DRUM -------------
POWER_LIMIT = 80        # Power limit = 80% 
SPEED_LIMIT = 1500       # Speed limit = 720dps | MAX = 1560 dps
MOTOR_POLL_DELAY = 0.01

DRUM = Motor('A')

def init_motor(motor: Motor):
    try: 
        motor.reset_encoder()                      # Reset encoder to 0 value
        motor.set_limits(POWER_LIMIT, SPEED_LIMIT) # Set power and speed limits
        motor.set_power(0)                         # Stop the motor as well
    except IOError as error:
        print(error)

def wait_for_motor(motor: Motor):
    "Function to block until motor completion"
    while math.isclose(motor.get_speed(), 0):    # Wait for motor to spin up   (start)
        time.sleep(MOTOR_POLL_DELAY)
    while not math.isclose(motor.get_speed(), 0):    # Wait for motor to spin down (stop)
        time.sleep(MOTOR_POLL_DELAY)

def reset_drum():
    DRUM.set_position(0)

def play_drum():
    pass




# ----------- EMERGENCY STOP -------------
def emergency_stop():

    pass
