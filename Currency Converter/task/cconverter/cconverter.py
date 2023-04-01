import sys

currencies_exchange = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17, 'AUD': 1.9622, 'MAD': 0.208}


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
    converter()


def user_input():
    # number_of_conicoins = str(input("Please, enter the number of conicoins you have: "))
    number_of_conicoins = str(input())
    # exchange_rate = str(input("Please, enter the exchange rate: "))

    # if ("." in number_of_conicoins) or ("." in exchange_rate):
    #     return float(number_of_conicoins), float(exchange_rate)
    # else:
    #     return int(number_of_conicoins), int(exchange_rate)
    return float(number_of_conicoins)


def converter():
    # number_of_conicoins, exchange_rate = user_input()
    number_of_conicoins = user_input()
    # print(f'The total amount of dollars: {(number_of_conicoins * exchange_rate)}')

    for c in currencies_exchange:
        print(
            f'I will get {round(number_of_conicoins * currencies_exchange[c], 2)} {c} from the sale of {number_of_conicoins} conicoins.')


if __name__ == "__main__":
    sys.exit(main())
