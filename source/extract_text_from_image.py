"""
This code uses the pytesseract library
and results in the text extracted from an image.

-> Requirements:
    . pip install pytesseract
"""

import pytesseract as ocr
from PIL import Image

text = ocr.image_to_string(Image.open('media/python.png'), lang='por+eng')

print(text)
