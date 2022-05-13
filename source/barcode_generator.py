"""
This code uses python-barcode and pillow libraries and results in a barcode.

-> Requirements:
    . pip install python-barcode
    . pip install pillow
"""

from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image  

number = '123456789012'  # needs 12 digits

barcode = EAN13(number, writer=ImageWriter())
barcode.save('barcode')

image = Image.open('barcode.png')
image.show()
