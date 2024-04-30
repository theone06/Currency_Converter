import requests


def retrieve_currency(held, wanted):
    response = requests.get(f'http://www.floatrates.com/daily/{held}.json')
    if response.status_code == 200:
        return response.json()[wanted]['rate']
    else:
        print('Failure!')
        exit()


held_currency = input().lower()

if held_currency == 'usd':
    currency_rate_cache = {'usd': 1, 'eur': retrieve_currency(held_currency, 'eur')}
elif held_currency == 'eur':
    currency_rate_cache = {'eur': 1, 'usd': retrieve_currency(held_currency, 'usd')}
else:
    currency_rate_cache = {'eur': retrieve_currency(held_currency, 'eur'),
                           'usd': retrieve_currency(held_currency, 'usd')}
while True:
    wanted_currency = input().lower()
    if wanted_currency == "":
        break
    amount_held = float(input())
    print("Checking the cache...")
    if wanted_currency in currency_rate_cache:
        print("Oh! It is in the cache!")
        print("You received", round(currency_rate_cache[wanted_currency] * amount_held, 2),
              wanted_currency.upper() + ".")
    else:
        print("Sorry, but it is not in the cache!")
        currency_rate_cache[wanted_currency] = retrieve_currency(held_currency, wanted_currency)
        print("You received", round(currency_rate_cache[wanted_currency] * amount_held, 2),
              "{0}.".format(wanted_currency.upper()))
