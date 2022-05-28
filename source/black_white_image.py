"""
This code uses the pillow library
and converts a color image to a black and white one.

-> Requirements:
    . pip install pillow
"""

from PIL import Image

image_color = Image.open('python_color.png')
image_no_color = image_color.convert('L')
image_no_color.save('python_no_color.png')

image_color.show()
image_no_color.show()
