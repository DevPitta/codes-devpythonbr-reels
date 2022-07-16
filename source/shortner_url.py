"""
This code uses the pyshorteners library
and results in a short url.

-> Requirements:
    . pip pyshorteners
"""


import pyshorteners

url = 'http://www.devpythonbr.com.br/blog/python-roadmap-o-caminho/6/'

s = pyshorteners.Shortener()

short_url = s.tinyurl.short(url)

print(f'URL encurtada: {short_url}')
