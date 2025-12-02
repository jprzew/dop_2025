import sys
import argparse


def add(x, y):
    return x + y


def product(x, y):
    return x * y


def divide(x, y):

    if y == 0:
        raise ValueError('We cannot divide by y = 0.')

    return x / y


def terminal_run():
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

# add,2,3

def read_configuration(path: str):

    with open(path, 'r') as f:
        line1 = f.read()

    operation, x, y = [element.strip() for element in  line1.split(',')]

    return {'operation': operation, 'x': x, 'y': y}


def run_from_file(path: str):
    conf = read_configuration(path)


    x = int(conf['x'])
    y = int(conf['y'])
    operation = conf['operation']
    if operation == 'add':
        result = add(x, y)
    elif operation == 'mul':
        result = product(x, y)
    else:
        print('Incorrect values in the config file.')
        return -1

    print(f'Your result: {result}')
    return 0


def main():

    parser = argparse.ArgumentParser(description='Simple calculator.')

    parser.add_argument(
        '--file',
        default='',
        help='Configuration file.'
    )

    args = parser.parse_args()

    if args.file == '':
        return terminal_run()

    return run_from_file(args.file)


if __name__ == '__main__':
    sys.exit(main())
