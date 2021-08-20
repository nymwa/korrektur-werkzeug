import sys
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--with-tag', action = 'store_true')
    return parser.parse_args()


def renversi(x):
    return x[::-1]


def renversi_with_tag(x):
    tag, rest = x[0], x[1:]
    return [tag] + rest[::-1]


def run_renversi(args, x):
    if args.with_tag:
        x = renversi_with_tag(x)
    else:
        x = renversi(x)
    return x


def main():
    args = parse_args()
    for line in sys.stdin:
        x = line.strip().split()
        x = run_renversi(args, x)
        x = ' '.join(x)
        print(x)

