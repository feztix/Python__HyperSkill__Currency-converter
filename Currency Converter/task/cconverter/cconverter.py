import sys


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
    converter()


def converter():
    currency = int(input())
    print(f'I have {currency} conicoins.')
    print(f'{currency} conicoins cost {currency * 100} dollars.')
    print(f'I am rich! Yippee!')


if __name__ == "__main__":
    sys.exit(main())
