"""
This code uses the forex-python library
and results in the conversion of dollars to reais.

-> Requirements:
    . pip install forex-python
"""

from forex_python.converter import CurrencyRates

currency = CurrencyRates()

value1 = float(input("\nWhat dollar amount do you want to convert to real? "))

value2 = round(currency.convert("USD", "BRL", value1), 2)

print(f"$ {value1:.2f} = R$ {value2:.2f}")
