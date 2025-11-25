import sys


def add(x, y):
    return x + y


def product(x, y):
    return x * y


def main():
    print('Select operation:')
    print(' 1. Addition')
    print(' 2. Multiplication')
    choice = input('Your choice: ')

    if choice not in ['1', '2']:
        print('Incorrect choice.')
        return -1

    x, y = eval(input('Enter numbers separated by a comma: '))

    if choice == '1':
        result = add(x, y)
    elif choice == '2':
        result = product(x, y)

    print(f'Your result: {result}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
