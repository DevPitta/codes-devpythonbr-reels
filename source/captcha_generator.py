"""
This code uses the captcha and pillow libraries
and results in an captcha image.

-> Requirements:
    . pip install captcha
    . pip install pillow
"""

from captcha.image import ImageCaptcha
from PIL import Image

image = ImageCaptcha(width=280, height=90)
captcha_text = 'DevPythonBr'
data = image.generate(captcha_text)
image.write(captcha_text, 'captcha.png')

captcha = Image.open('captcha.png')
captcha.show()
