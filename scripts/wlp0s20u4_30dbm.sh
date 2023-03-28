#!/bin/bash

# Check if script is run with sudo privileges
if [ "$EUID" -ne 0 ]
  then echo "Please run as root or with sudo privileges!"
  exit
fi

# Turn off wireless interface, set regulatory domain to Bolivia, set TX power to 30 dBm, and turn it back on
echo "Turning off wireless interface and setting regulatory domain to Bolivia..."
sudo ifconfig wlp0s20u4 down && sudo iw reg set BO && sudo iwconfig wlp0s20u4 txpower 30 && sudo ifconfig wlp0s20u4 up

# Show wireless interface information
echo "Wireless interface information:"
iwconfig
