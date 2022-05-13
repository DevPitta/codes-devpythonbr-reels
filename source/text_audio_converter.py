"""
This code uses the gTTs
and playsound libraries
and results in transforming text into speech.

-> Requirements:
    . pip install gTTs
    . pip install playsound
"""

import gtts
from playsound import playsound

tts = gtts.gTTS('Bem vindo a DevPythonBr. Me siga para aprender mais sobre programação', lang='pt-br')
tts.save('devpythonbr.mp3')
playsound('devpythonbr.mp3')
