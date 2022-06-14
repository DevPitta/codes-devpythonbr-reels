"""
This code uses the webbrowser, pillow and pyzbar libraries
and reads a qrcode.

-> Requirements:
    . pip install pillow
    . pip install pyzbar
    . sudo apt-get install zbar-tools
"""

import webbrowser
from PIL import Image
from pyzbar.pyzbar import decode

read = decode(Image.open('qrcode_devpythonbr.png'))
webbrowser.open_new(read[0].data.decode('ascii'))
