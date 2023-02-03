#!/usr/bin/env python3

"""
Module to play sounds when the touch sensor is pressed.
This file must be run on the robot.
"""
 
from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors
import time

SOUND = sound.Sound(duration=0.3, pitch="A4", volume=200)
TOUCH_SENSOR = TouchSensor(1)

# C = sound.Sound(duration=0.3, pitch="C3", volume=200)
# D = sound.Sound(duration=0.3, pitch="D3", volume=200) 
# E = sound.Sound(duration=0.3, pitch="E3", volume=200) 
# F = sound.Sound(duration=0.3, pitch="F3", volume=200) 
# G = sound.Sound(duration=0.3, pitch="G3", volume=200) 
# A = sound.Sound(duration=0.3, pitch="A3", volume=200) 
# B = sound.Sound(duration=0.3, pitch="B4", volume=200) 
# C2 = sound.Sound(duration=0.3, pitch="C4", volume=200) 
# D2 = sound.Sound(duration=0.3, pitch="D4", volume=200) 
# 


wait_ready_sensors() # Note: Touch sensors actually have no initialization time

rick_roll = [["D3", 0.3],["E3", 0.3],["F3", 0.3],["D3", 0.3],["A3", 0.3],["A3", 0.3],["G3", 0.3]]
note_sounds = [sound.Sound(duration=dura, pitch=note, volume=100) for note, dura in rick_roll]


RICKROLL=sound.Song(rick_roll)
RICKROLL.compile()


def play_sound():
    "Play a single note."
    RICKROLL.play()
    RICKROLL.wait_done()
#     D.play()
#     D.wait_done()
#     E.play()
#     E.wait_done()
#     F.play()
#     F.wait_done()
#     D.play()
#     D.wait_done()
#     A.play()
#     A.wait_done()
#     A.play()
#     A.wait_done()
#     G.play()
#     G.wait_done()


def play_sound_on_button_press():
    "In an infinite loop, play a single note when the touch sensor is pressed."
    try:
        while True:
            if TOUCH_SENSOR.is_pressed():
                play_sound()
    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        exit()


if __name__=='__main__':
    play_sound()

    # TODO Implement this function
    play_sound_on_button_press()

