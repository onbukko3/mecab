import konlpy
from konlpy.tag import Mecab
import time

kor_dict='/usr/local/lib/mecab/dic/mecab-ko-dic'
filename = 'test.ko'

mecab = Mecab(dicpath=kor_dict)
# sent = "우리는 현재 독일에서 거주하고 있어요."
# print(sent)

# print(mecab.morphs(sent))
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

if __name__ == "__main__":
    
    with open(filename, 'r') as src:
        with open(filename+".morphs", 'w') as tgt:
            start_time = time.time()
            for line in src.readlines():
                print(' '.join(tokenize(line))+'\n')
                tgt.write(' '.join(tokenize(line))+'\n')
            print("time: {}".format(time.strftime("%H:%M:%S", time.gmtime(time.time()-start_time))))
        