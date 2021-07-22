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
        self.dct = defaultdict(list)

    def add(self, sent):
        self.dct[sent.index].append(sent)

    def as_list(self):
        data = list(self.dct.items())
        data.sort()
        data = [sent_to_dict(key, value) for key, value in data]
        return data


class Sentence:
    def __init__(self, index, score, text):
        self.index = index
        self.score = score
        self.text = text

    def __lt__(self, other):
        return self.score < other.score

    def as_dict(self):
        return {'score': self.score, 'text': self.text}


def load_fairseq_generate_output():
    for x in sys.stdin:
        if x.startswith('H'):
            x = x.split('\t')
            index = int(x[0].split('-')[1])
            score = float(x[1])
            text = x[2].strip()
            yield Sentence(index, score, text)


def make_data(sent_list):
    data = Data()
    for sent in sent_list:
        data.add(sent)
    return data


def main():
    sent_list = load_fairseq_generate_output()
    data = make_data(sent_list)
    data = data.as_list()
    yml = yaml.safe_dump(data, allow_unicode = True)
    print(yml)

