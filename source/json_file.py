"""
This code uses json library
and results in a json file.
"""

import json

data = {
    'nome': 'Adm',
    'instagram': 'DevPythonBr',
    'linguagem': 'Python',
    'conteudos': [
        {'posts': 'informativos'},
        {'reels': 'codigos'}
    ]
}

with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
