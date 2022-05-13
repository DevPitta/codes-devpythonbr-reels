"""
This code generates random passwords.
"""

from random import sample
from string import ascii_letters

letters = ascii_letters
numbers = '0123456789'
specials = '-+*%&$!_'
lne = letters + numbers + specials

password_length = int(input('Enter password length: '))

password = ("".join(sample(lne, password_length)))

print(f'Password: {password}')
