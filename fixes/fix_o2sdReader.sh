#!/bin/bash

#
# very simple fix for O2 Micro, Inc. SD/MMC Card Reader Controller
# gh: ysfsvm

# One time only fix
# sudo rmmod sdhci_pci sdhci_acpi sdhci
# sudo modprobe sdhci debug_quirks2="0x80000000"
# sudo modprobe sdhci_pci
#
# source: https://www.linuxquestions.org/questions/linux-laptop-and-netbook-25/sd-card-reader-o2-micro-not-working-4175663053/

RED='\033[1;31m'
GREEN='\033[1;92m'
CYAN='\033[1;36m'
YELLOW='\033[1;93m'
NOCOLOR='\033[0m'

if [ "$EUID" -ne 0 ]
  then echo -e "Please run as ${RED}ROOT${NOCOLOR}"
  exit
fi

echo -e "${GREEN}Adding sdhci_pci to modules-load.d for autostart...${NOCOLOR}"
echo sdhci_pci > /etc/modules-load.d/sdhci_pci.conf
echo -e "${CYAN}DONE!${NOCOLOR}"

echo -e "\n${GREEN}Adding config for sdhci to modules-load.d for fix...${NOCOLOR}"
echo "options sdhci debug_quirks2=0x80000000" >> /etc/modprobe.d/sdhci.conf
echo -e "${CYAN}DONE!${NOCOLOR}"

echo -e "\n${YELLOW}Sd card should work now!${NOCOLOR}"
