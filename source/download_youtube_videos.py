"""
This code uses the pytube library
and results in a youtube video download.

-> Requirements:
    . pip install pytube
"""

from pytube import YouTube

YouTube('https://www.youtube.com/watch?v=-LATVnPcvHI&t=2s&ab_channel=AluraCursosOnline').streams.get_highest_resolution().download()
