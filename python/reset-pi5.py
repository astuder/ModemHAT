#!/usr/bin/python

# Reset the modem HAT on a Raspberry Pi 5

import gpiod
import time
chip = gpiod.Chip('gpiochip4')
reset = chip.get_line(25)
reset.request(consumer='rst', type=gpiod.LINE_REQ_DIR_OUT)
reset.set_value(0)
time.sleep(0.5)
reset.set_value(1)
time.sleep(0.3)
