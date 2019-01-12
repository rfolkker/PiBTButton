#!/usr/bin/env python

import sys
import evdev
import subprocess

devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
if len(devices) == 0:
    print "No devices found, kicking Bluetooth"
    subprocess.call(['./init.sh'])
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    
if len(devices) == 0:
    print "No devices found, try running with sudo"
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
                    if event.code == 28:
                        print("Button2 Pressed")
