import sys
import yaml
from collections import defaultdict

def make_sent_dict_list(sent_list):
    return [sent.as_dict() for sent in sent_list]


def sent_to_dict(key, value):
    hypos = make_sent_dict_list(value)
    return {'index': key, 'hypos': hypos}


class Data:
    def __init__(self):
        self.dct = defaultdict(dict)

    def add_source(self, index, text):
        self.dct[index]['index'] = index
        self.dct[index]['source'] = text

    def add_hypothesis(self, index, score, text):
        if 'hypos' not in self.dct[index]:
            self.dct[index]['hypos'] = []
        self.dct[index]['hypos'].append(
                {'score': score, 'text': text})

    def as_list(self):
        lst = []
        for key, value in self.dct.items():
            lst.append(value)
        lst.sort(key = lambda x: x['index'])
        return lst


def main():
    data = Data()

    for x in sys.stdin:
        if x.startswith('S'):
            x = x.rstrip('\n').split('\t')
            index = int(x[0].split('-')[1])
            text = x[1]
            data.add_source(index, text)
        elif x.startswith('H'):
            x = x.rstrip('\n').split('\t')
            index = int(x[0].split('-')[1])
            score = float(x[1])
            text = x[2]
            data.add_hypothesis(index, score, text)

    data = data.as_list()
    yml = yaml.safe_dump(data, allow_unicode = True)
    print(yml)

