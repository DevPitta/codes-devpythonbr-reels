"""
This code uses the pillow library
and results in the resized image.

-> Requirements:
    . pip install pillow
"""

from PIL import Image

base_width = 400
image = Image.open('image.jpg')
width_percentage = (base_width / float(image.size[0]))
altura = int((float(image.size[1]) * float(width_percentage)))
resized_image = image.resize((base_width, altura), Image.Resampling.LANCZOS)
resized_image.save('resized_image.jpg')
image.show()
resized_image.show()
