import sys
import yaml
from argparse import ArgumentParser
from reguligilo.decoder import Decoder

space = chr(0x2581)
decoder = Decoder()


def reverse_sent(x):
    x = x.strip().split()[::-1]
    x = ' '.join(x)
    return x


def remove_bpe(x):
    x = x.strip()
    x = x.split()
    x = ''.join(x)
    x = x.replace(space, ' ')
    x = x.strip()
    return x


def sort_by_score(lst):
    lst.sort(key=lambda x : x['score'])


def print_best(args, lst):
    x = lst[-1]['text']

    if args.reverse:
        x = reverse_sent(x)

    if not args.retain_whitespace:
        x = remove_bpe(x)

    if not args.retain_normalized:
        x = decoder(x)

    if args.show_score:
        score = lst[-1]['score']
        x = '{}\t{}'.format(score, x)

    print(x)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-s', '--show-score', action = 'store_true')
    parser.add_argument('-r', '--reverse', action = 'store_true')
    parser.add_argument('--retain-whitespace', action = 'store_true')
    parser.add_argument('--retain-normalized', action = 'store_true')
    return parser.parse_args()


def main():
    args = parse_args()

    yml = yaml.safe_load(sys.stdin)

    for hypos_dict in yml:
        hypos = hypos_dict['hypos']
        sort_by_score(hypos)
        print_best(args, hypos)

