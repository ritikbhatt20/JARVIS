from forex_python.converter import CurrencyRates

def currency_conversion(amount, from_currency, to_currency):
    c = CurrencyRates()
    result = c.convert(from_currency, to_currency, amount)
    return result 