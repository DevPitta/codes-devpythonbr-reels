"""
This code uses the wikipedia library and performs a keyword search in wikipedia.

-> Requirements:
    . pip install wikipedia
"""

import wikipedia

wikipedia.set_lang("pt")

search = wikipedia.summary("python")
print(search)
