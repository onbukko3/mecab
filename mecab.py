import sys
import konlpy
from konlpy.tag import Mecab

src = sys.argv[1]
tgt = sys.argv[2]

kor_dict='/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ko-dic'

mecab = Mecab(dicpath=kor_dict)

def tokenize(sent):
    token = []
    sent_nr = 0
    for mor in mecab.parse(sent).split('\n'):
        # print(mor)
        if '\t' in mor:
            splitted = mor.split('\t')
            morph = splitted[0]
            if sent[sent_nr] == ' ':
                token.append('▃')
                sent_nr += 1
            token.append(morph)
            sent_nr += len(morph)
    return token

with open(src, 'r') as src:
    with open(tgt, 'w') as tgt:
        print("-----------------Mecab--------------")
        for line in src.readlines():
            token=tokenize(line)
            tgt.write(' '.join(token)+'\n')
        print("-----------------finished--------------")
        tgt.close()
    src.close()
        