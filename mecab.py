import konlpy
from konlpy.tag import Mecab

kor_dict='/usr/local/lib/mecab/dic/mecab-ko-dic'
filename = 'test.ko'

mecab = Mecab(dicpath=kor_dict)
with open(filename, 'r') as src:
    with open(filename+".morphs", 'w') as tgt:
        for line in src.readlines():
            tgt.write(' '.join(mecab.morphs(line))+'\n')
        