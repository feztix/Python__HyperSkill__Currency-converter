import sys

import requests

currencies_exchange = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17, 'AUD': 1.9622, 'MAD': 0.208}


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
    converter()


def user_input():
    # number_of_conicoins = str(input())
    currency = str(input())

    return currency


def converter():
    currency = user_input()

    r = requests.get(f'http://www.floatrates.com/daily/{currency}.json').json()
    print(r['usd'])
    print(r['eur'])

    # for c in currencies_exchange:
    #     print(
    #         f'I will get {round(number_of_conicoins * currencies_exchange[c], 2)} {c} from the sale of {number_of_conicoins} conicoins.')


if __name__ == "__main__":
    sys.exit(main())
