import sys
from argparse import ArgumentParser
from collections import defaultdict

def reverse_text(text, with_tag = False):
    if with_tag:
        text = text.split()
        tag, rest = text[0], text[1:]
        text = [tag] + rest[::-1]
    else:
        text = text.split()[::-1]
    return ' '.join(text)


class Data:
    def __init__(self, with_tag = False):
        self.with_tag = with_tag
        self.dct = defaultdict(dict)

    def add_source(self, index, text):
        self.dct[index]['source'] = reverse_text(text, with_tag = self.with_tag)

    def add_hypothesis(self, index, score, text):
        self.dct[index]['score'] = score
        self.dct[index]['hypothesis'] = reverse_text(text)

    def show(self):
        lst = [(key, value) for key, value in self.dct.items()]
        lst.sort(key = lambda x: x[0])

        for key, value in lst:
            source = value['source']
            score = value['score']
            hypothesis = value['hypothesis']
            print('{}\t{}\t{}'.format(score, source, hypothesis))

def main():
    parser = ArgumentParser()
    parser.add_argument('--with-tag', action = 'store_true')
    args = parser.parse_args()

    data = Data(with_tag = args.with_tag)

    for x in sys.stdin:
        if x.startswith('S'):
            x = x.split('\t')
            index = int(x[0].split('-')[1])
            text = x[1].strip()
            data.add_source(index, text)
        elif x.startswith('H'):
            x = x.split('\t')
            index = int(x[0].split('-')[1])
            score = float(x[1])
            text = x[2].strip()
            data.add_hypothesis(index, score, text)

    data.show()

