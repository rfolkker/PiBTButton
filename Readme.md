# Raspberry Pi hat sample project #

## Brief: ##
This is a Python3 application to allow a user to trigger a hat via a servo and motor hat stacked on a Raspberry Pi 3

There are three primary components to make this project work

* The environment
* The Python Script and bluetooth connector
* The Service

## The Environment ##
The environment is the isolation of the Python required libraries.
Activate the environment directly by executing

    source env/bin/activate   

The environment is triggered when the service starts.

This *should* include a requirements.txt file
Install via:

    pip3 install -r requirements.txt

## The Python Script and bluetooth connector ##

There is an init.sh script that must have exeuction permissions

    chmod +644 ./init.sh

This script forces the connection to the Bluetooth device and is executed whenever the device wakes back up.
This allows for the BLE power-saving mode on the Bluetooth button (it does not save energy on the RPi)

There is a hat.py file that actually monitors and reacts to button presses on the Bluetooth device.
This file should also have execution permission

    chmod +644 ./hat.py

There are other files in this folder, most to practice and test activites. They are not actively used.
With exception to the service file, which is covered below

## The Service ##
There is a hat.service file located in the root folder.  This file needs to be copied into the systemd service folder

    sudo cp ./hat.service /lib/systemd/system/hat.service

From there, you will need to set the permissions on the file

    chmod +644 /lib/systemd/system/hat.service

Now refresh your systemd environment, enable and start the service.

    sudo systemctl daemon-reload
    sudo systemctl enable hat.service
    sudo systemctl start hat.service

## Summary ##

This completes the basic setup. By following and configuring the information above, you should be good to go.
