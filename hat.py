#!./env python

import sys
import evdev
import subprocess
import board
import busio
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c, address=0x41)
hat.frequency = 60
led_channel = hat.channels[0]

## kit = ServoKit(channels=8, address=0x41)

def trigger_servo():
    kit.servo[0].angle = 180
    kit.continuous_servo[1].throttle = 1
    time.sleep(5)
    kit.servo[0].angle = 0
    kit.continuous_servo[1].throttle = 0

def brighten_led():
    # Increase brightness:
    for i in range(0,0xffff,0xf):
        led_channel.duty_cycle = i
    # print("complete")

def darken_led():
    # Decrease brightness:
    for i in range(0xffff, 0, -0xf):
        led_channel.duty_cycle = i
    # print("complete")

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

        for device in devices:
            if device.name == 'AB Shutter 3':
                # print(device)
                device.grab()
                for event in device.read_loop():
                    if event.type == evdev.ecodes.EV_KEY:
                        if event.value == 0:
                            if event.code == 115:
                                # print("Button1 Pressed")
                                brighten_led()
                            if event.code == 28:
                                # print("Button2 Pressed")
                                darken_led()
    except KeyboardInterrupt:
        # print("Exiting.")
        # sys.exit(1)
        # print("Service does not exit")
        pass
    except:
        # print("An error occurred")
        pass
## End of While
