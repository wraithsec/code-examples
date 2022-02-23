#!/usr/bin/python3
import argparse


def task_a(alpha):
    print('task a', alpha)


def task_b(beta, gamma):
    print('task b', beta, gamma)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser')

    parser_a = subparsers.add_parser('task_a')
    parser_a.add_argument(
        '-a', '--alpha', dest='alpha', help='Alpha description')

    parser_b = subparsers.add_parser('task_b')
    parser_b.add_argument(
        '-b', '--beta', dest='beta', help='Beta description')
    parser_b.add_argument(
        '-g', '--gamma', dest='gamma', default=42, help='Gamma description')

    kwargs = vars(parser.parse_args())
    globals()[kwargs.pop('subparser')](**kwargs)
