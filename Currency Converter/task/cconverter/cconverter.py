# import sys
#
# import requests
#
# currencies_exchange = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17, 'AUD': 1.9622, 'MAD': 0.208}
#
#
# def main(args=None):
#     """The main routine."""
#     if args is None:
#         args = sys.argv[1:]
#     converter()
#
#
# def user_input():
#     # number_of_conicoins = str(input())
#     currency = str(input())
#
#     return currency
#
#
# def converter():
#     currency = user_input()
#
#     r = requests.get(f'http://www.floatrates.com/daily/{currency}.json').json()
#     print(r['usd'])
#     print(r['eur'])
#
#     # for c in currencies_exchange:
#     #     print(
#     #         f'I will get {round(number_of_conicoins * currencies_exchange[c], 2)} {c} from the sale of {number_of_conicoins} conicoins.')
#
#
# if __name__ == "__main__":
#     sys.exit(main())

import requests
import json

source_code = input().lower()
url = f'http://www.floatrates.com/daily/{source_code}.json'
response = requests.get(url)
data = json.loads(response.text)

rates = {}
if source_code != 'usd':
    rates['usd'] = data['usd']['rate']
if source_code != 'eur':
    rates['eur'] = data['eur']['rate']

while target_code := input().lower():
    amount = int(input())

    print('Checking the cache...')
    rate = rates.get(target_code, 0)
    if rate:
        print('Oh! It is in the cache!')
    else:
        print('Sorry, but it is not in the cache!')
        rate = data[target_code]['rate']
        rates[target_code] = rate

    print(f'You received {amount * rate:.2f} {target_code.upper()}.')