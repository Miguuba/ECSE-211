#!/usr/bin/python3
import musical_buttons
import motors

if __name__=='__main__':
    # global CURRENT_NOTE
    # global STATE

    # STATE = 0 # default status = 0, no button is pressed
    # CURRENT_NOTE = flute.note_sounds[0] # will be dynamically updated its reference
    
    try:
        motors.init_motor(motors.RED_MOTOR)

        while True:
            #value = flute.play(STATE, CURRENT_NOTE)
            value = musical_buttons.play()
            # STATE = value[0]
            # CURRENT_NOTE = value[1]
            if value == -1:
                print("Emergency button pressed! Exiting...")
                exit()
            
            if musical_buttons.DRUM == True:
                motors.rotate_RED_MOTOR(45, 400)

    except BaseException as e:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        motors.BP.reset_all()
        print(e)
        print("Exception encountered (see above), exiting!")
        exit()
