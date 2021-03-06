#!/usr/bin/env python

import sys
import evdev
import subprocess
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=8, address=0x41)

def trigger_servo():
    kit.servo[0].angle = 180
    kit.continuous_servo[1].throttle = 1
    time.sleep(5)
    kit.servo[0].angle = 0
    kit.continuous_servo[1].throttle = 0

while(1):
    try:
        devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        if len(devices) == 0:
            print ("No devices found, kicking Bluetooth")
            subprocess.call(['./init.sh'])
            devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

        if len(devices) == 0:
            print ("No devices found, try running with sudo")
            sys.exit(1)

        for device in devices:
            if device.name == 'AB Shutter 3':
                print(device)
                device.grab()
                for event in device.read_loop():
                    if event.type == evdev.ecodes.EV_KEY:
                        if event.value == 0:
                            if event.code == 115:
                                print("Button1 Pressed")
                                trigger_servo()
                            if event.code == 28:
                                print("Button2 Pressed")
    except KeyboardInterrupt:
        print("Exiting.")
        sys.exit(1)
    except:
        print("An error occurred")
## End of While
