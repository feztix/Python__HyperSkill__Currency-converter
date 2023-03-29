import sys


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
    converter()


def user_input():
    number_of_conicoins = str(input("Please, enter the number of conicoins you have: "))
    exchange_rate = str(input("Please, enter the exchange rate: "))

    if ("." in number_of_conicoins) or ("." in exchange_rate):
        return float(number_of_conicoins), float(exchange_rate)
    else:
        return int(number_of_conicoins), int(exchange_rate)


def converter():
    number_of_conicoins, exchange_rate = user_input()
    print(f'The total amount of dollars: {(number_of_conicoins * exchange_rate)}')


if __name__ == "__main__":
    sys.exit(main())
