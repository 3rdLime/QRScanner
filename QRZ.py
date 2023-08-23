#!/usr/bin/env python3
 
# ------------------------------------------------------------------------
# Created By: 3rdLime
# Created Date: 08/22/2023
# Version: 1.0
# ------------------------------------------------------------------------
#
# This script grabs a QR code link and pops open a VirusTotal window so 
# you can copy and pasta to check if the QR code is mostly safe. 
#
# Make sure that your image file is in the local directory or you 
# use the full directory path.
#
# To Do List:
#    Perform module validation and load if missing.
#    Auto-launch the URL in virus total.
#    Clean up for sensitive eyeballz.
#


import webbrowser
from PIL import Image
from pyzbar.pyzbar import decode

url = "https://www.virustotal.com/gui/home/url"

filepath = input('What is your filename?\n')

data = decode(Image.open(filepath))[0][0]

print(data)

webbrowser.open(url, new=1, autoraise=True)

print("Now copy and paste that shit to see if its bad!")
