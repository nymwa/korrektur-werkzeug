import sys
from collections import defaultdict

def reverse_text(text):
    text = text.split()[::-1]
    return ' '.join(text)


class Data:
    def __init__(self):
        self.dct = defaultdict(dict)

    def add_source(self, index, text):
        self.dct[index]['source'] = reverse_text(text)

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
    data = Data()

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
