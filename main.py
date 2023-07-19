from forex_python.converter import CurrencyRates

def convert_currency():
    try:
        c = CurrencyRates()
        print("Доступные валюты:")
        for currency in c.get_rates('USD'):
            print(currency)

        base_currency = input("Введите базовую валюту (например, USD): ").upper()
        target_currency = input("Введите целевую валюту (например, EUR): ").upper()
        amount = float(input("Введите сумму для конвертации: "))

        converted_amount = c.convert(base_currency, target_currency, amount)
        print(f"{amount} {base_currency} равны {converted_amount} {target_currency}")

    except Exception as e:
        print("Произошла ошибка:", e)

if __name__ == "__main__":
    convert_currency()
