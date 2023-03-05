#!/usr/bin/python3
 
import time
from utils.sound import Sound
from utils.brick import TouchSensor
from time import sleep
# Create sound variables
notes = ['C4','D4','E4','F4','G4','A4','B4','C5']
note_sounds = [Sound(duration=2, pitch=note, volume=90) for note in notes]
# note001 = Sound(duration=0.0001, pitch="F#4", volume=100)

# Create STM Song
# STM = Song(note_sounds)
TS_S1 = TouchSensor(1)
TS_S2 = TouchSensor(2)
TS_S3 = TouchSensor(3)
TS_S4 = TouchSensor(4) # Emergency stop


def combo_state():
    combo = [int(TS_S1.is_pressed()), int(TS_S2.is_pressed()), int(TS_S3.is_pressed())]
    if combo == [1,1,1]: # play DRUM!
        return 7
    elif combo == [1,0,1]: # play note 6 ! I think this should be the drum combo
        return 6
    elif combo == [0,1,1]: # play note 5
        return 5
    elif combo == [1,1,0]: # play note 4
        return 4
    elif combo == [0,0,1]: # play note 3
        return 3
    elif combo == [0,1,0]: # play note 2
        return 2
    elif combo == [1,0,0]: # play note 1
        return 1
    return 0


def music_stop():
    # Will be used in WaddleBand.py
    pass    

STATE = 0 # default status = 0, no button is pressed
CURRENT_NOTE = note_sounds[0] # will be dynamically updated its reference

def play():
    global CURRENT_NOTE 
    # CURRENT_NOTE = currentNote
    global STATE 
    # STATE = state
    try:
        if(TS_S4.is_pressed()):
            return -1
        else:
                # Method: debounce the signal
            old_state = STATE
            time.sleep(0.05) # debouncing the signal, time decided on human reaction time
            STATE = combo_state()
            # print(f'{STATE}')
            isNewState = (old_state != STATE)
                
            # ------------- Condition diagram 2 ------------- #
            if isNewState:
                print(f'New State: {STATE}')
                if CURRENT_NOTE.is_playing():
                    CURRENT_NOTE.stop()
                if STATE != 0:
                    # play new note
                    CURRENT_NOTE = note_sounds[STATE-1]
                    CURRENT_NOTE.play()
            else: # same state
                # TODO: keep playing the note
                if STATE != 0:    
                    if CURRENT_NOTE.is_playing():
                        CURRENT_NOTE.stop()
                    else:
                        CURRENT_NOTE.play()

    except BaseException as e:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        print(e)
        print("exiting!")
        exit()
    
    return (CURRENT_NOTE, STATE)


if __name__=='__main__':
    print("Press something!")
    play()
