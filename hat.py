#!./env python

import sys
import evdev
import subprocess
import board
import busio
import datetime
from adafruit_servokit import ServoKit
from adafruit_motorkit import MotorKit

servo_kit = ServoKit(channels=8, address=0x41)
motor_kit = MotorKit()

motor_start = 0
motor_check = 0
servo_start = 0
servo_check = 0

## kit = ServoKit(channels=8, address=0x41)

def trigger_servo():
    servo_kit.servo[0].angle = 180
    servo_start = datetime.datetime.now()

def reset_servo():
    servo_kit.servo[0].angle = 0
    servo_start = 0
    servo_end = 0

def trigger_motor():
    motor_kit.motor2.throttle = 1.0
    motor_start = datetime.datetime.now()

def reset_motor():
    motor_kit.motor2.throttle = 0.0
    motor_start = 0
    motor_end = 0

motor_kit.motor2.throttle = 0
servo_kit.servo[0].angle = 0

while(1):
    try:
        devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        if len(devices) == 0:
            # print ("No devices found, kicking Bluetooth")
            subprocess.call(['./init.sh'])
            devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

        if len(devices) == 0:
            # print ("No devices found, try running with sudo")
            sys.exit(1)

        # Check to see if the servo has fired
        # If it has, make sure it only runs for 10 seconds
        # if(servo_start != 0):
        #    servo_check = datetime.datetime.now() - servo_start
        #    if(servo_check.seconds > 10):
        #        reset_servo()

        # Check to see if the motor has fired
        # If it has, make sure it only runs for 10 seconds
        # if(motor_start != 0):
        #    motor_check = datetime.datetime.now() - motor_start
        #    # print("Motor running for "+motor_check.seconds+ " seconds")
        #    if(motor_check.seconds > 10):
        #        reset_motor()

        for device in devices:
            if device.name == 'AB Shutter 3':
                # print(device)
                device.grab()
                for event in device.read_loop():
                    if event.type == evdev.ecodes.EV_KEY:
                        if event.value == 0:
                            if event.code == 115:
                                # print("Button1 Pressed")
                                trigger_servo()
                                # print(servo_start)
                                trigger_motor()
                                # print(motor_start)
                            if event.code == 28:
                                reset_servo()
                                reset_motor()
                                # print("Button2 Pressed")
    except KeyboardInterrupt:
        # print("Exiting.")
        # sys.exit(1)
        # print("Service does not exit")
        pass
    except:
        # print("An error occurred")
        pass
## End of While
