#!/usr/bin/python3

import utils.brick as ub
import time

touches = [ub.TouchSensor(i) for i in range(1,5)]

motor = ub.brick.Motor('A')

ub.wait_ready_sensors()
