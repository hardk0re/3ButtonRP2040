# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import digitalio
import usb_hid
from   adafruit_hid.keyboard import Keyboard
from   adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

# define buttons. these can be any physical switches/buttons, but the values
# here work out-of-the-box with a CircuitPlayground Express' A and B buttons.
lft = digitalio.DigitalInOut(board.A2)
lft.direction = digitalio.Direction.INPUT
lft.pull = digitalio.Pull.UP

toe = digitalio.DigitalInOut(board.A3)
toe.direction = digitalio.Direction.INPUT
toe.pull = digitalio.Pull.UP

rght = digitalio.DigitalInOut(board.A1)
rght.direction = digitalio.Direction.INPUT
rght.pull = digitalio.Pull.UP


while True:
    # press ALT+TAB to swap windows
    if not lft.value:
        kbd.press(Keycode.F7)

    if lft.value:
        kbd.release(Keycode.F7)
        
    if not toe.value:
        kbd.press(Keycode.F8)

    if toe.value:
        kbd.release(Keycode.F8)

    if not rght.value:
        kbd.press(Keycode.F9)

    if rght.value:
        kbd.release(Keycode.F9)


    time.sleep(0.01)

