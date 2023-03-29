#!/bin/python3

#----------------------------------------------------------------------------
# Created By  : github/a && modified by github/ysfsvm
# Created Date: 29.03.2023
# license = MIT
# Main code and all api from https://gitlab.com/a/PTT-API
# Just little colorful and modified version
#----------------------------------------------------------------------------


import sys
import requests
from prettytable import PrettyTable
from termcolor import colored

user_agent = "ek.ptt"
general_url = "https://pttws.ptt.gov.tr/cepptt/mssnvrPttaceaemaa/gonderitakipvepostakod/gonderisorguYurticiveYurtDisi"
headers = {"User-Agent": user_agent}


def do_query(barcode):
    r = requests.post(general_url, data={"kaynak": "ANDROID", "barkod": barcode, "tokenIdBildirim": ""}, headers=headers)
    return r.json()


if __name__ == "__main__":
    # Verify that we can get the tracking code
    if len(sys.argv) < 2:
        print(colored(f"Usage: {sys.argv[0]} TRACKINGCODE", "red"))
        sys.exit(1)

    # Get the tracking code
    barcode = sys.argv[1]

    # Make the API do a smart query
    barcode_info = do_query(barcode)

    # Extract sender, recipient, and barcode information
    sender = barcode_info["GONDEREN"]
    recipient = barcode_info["ALICI"]
    barcode_number = barcode_info["BARNO"]
    payment = barcode_info.get("GONUCR") + "TL"

    # Print sender, recipient, and barcode information
    # Print sender, recipient, and barcode information
    print(colored(f"\nGönderen: {colored(sender, 'magenta')}", "green"))
    print(colored(f"Alıcı: {colored(recipient, 'yellow')}", "green"))
    print(colored(f"Barkod numarası: {colored(barcode_number, 'cyan')}", "green"))
    print(colored(f"Gönderi Ücreti: {colored(payment, 'blue')}\n", "green"))


    # Create a table to display the data
    table = PrettyTable()
    table.field_names = [colored("İşlem Ayrıntısı", "cyan"), colored("İşlem Tarihi/Saati", "cyan"), colored("Ofis", "cyan")]

    # Go through the events if there's any and print them out
    events = barcode_info["dongu"]
    if events:
        for event in events:
            detail = event.get("event", event.get("ISLEM")).strip()
            timestamp = event.get("tarih", event.get("ITARIH") + " " + event.get("ISAAT"))
            ofis = event.get('ofis', event.get('IMERK', ''))
            table.add_row([detail, timestamp, ofis])
    else:
        print(colored("No data yet.", "red"))

    # Print the table
    print(table)
    print()
