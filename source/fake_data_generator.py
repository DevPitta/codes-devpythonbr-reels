"""
This code uses the faker library
and results in the generation of false data.

-> Requirements:
    . pip install faker
"""

from faker import Faker

fake = Faker('pt-BR')

name = fake.name()
address = fake.address()
email = fake.email()

print(f'Name: {name}')
print(f'Address: {address}')
print(f'E-mail: {email}')
print('-=' * 30)

profile = fake.profile()
for k, v in profile.items():
    print(f'{k}: {v}')
