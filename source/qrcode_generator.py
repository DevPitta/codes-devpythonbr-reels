"""
This code uses qrcode and pillow libraries and results in a QRCode.

-> Requirements:
    . pip install qrcode
    . pip install pillow
"""

import qrcode

devpythonbr_qrcode = qrcode.make('http://www.devpythonbr.com.br')
devpythonbr_qrcode.save('qrcode_devpythonbr.png')
