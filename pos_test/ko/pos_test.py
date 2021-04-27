import argparse
import konlpy
from konlpy.tag import Mecab

parse = argparse.ArgumentParser()
parse.add_argument('-s',dest='src')
parse.add_argument('-b',dest='bpe')
parse.add_argument('-t',dest='tgt')

args = parse.parse_args()

kor_dict='/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ko-dic'

mecab = Mecab(dicpath=kor_dict)

def tokenize(sent):
    token = []
    tags = []
    sent_nr = 0
    for mor in mecab.parse(sent).split('\n'):
        # print(mor)
        if '\t' in mor:
            splitted = mor.split('\t')
            morph = splitted[0]
            tag = splitted[1].split(',')[0]
            if sent[sent_nr] == ' ':
                token.append('▃')
                tags.append('WSP')
                sent_nr += 1
            token.append(morph)
            tags.append(tag)
            # print(morph, tag)
            sent_nr += len(morph)
    return token, tags

def tag_inserting(bpe_tokens, tags):

    total = []
    i=0
    # print(tags)
    # print(bpe_tokens)
    for tok in bpe_tokens:
        if '@@' in tok:
            # print(tok)
            total.append(tags[i])
        else:
            # print(len(bpe_tokens), len(tags), i , tok, tags[i])
            
            # if tok == '▃':
            #     # print(tok, tags[i])
            #     total.append(tok)
            #     i += 1
            # else:
            # total.append(tok)
            total.append(tags[i])
            i += 1
    return total

def main():

    with open(args.src , 'r') as src, open(args.bpe, 'r') as bpe, open(args.tgt, 'w') as tgt:

        for src_line, bpe_line in zip(src.readlines(), bpe.readlines()):
            # print(src_line.strip('\n'))
            # print(bpe_line.strip('\n'))
            _ , tags = tokenize(src_line.strip('\n'))
            # print(token)
            bpe_tokens = bpe_line.strip('\n').split(' ')
            total = tag_inserting(bpe_tokens, tags)
            if len(total) != len(bpe_tokens):
                print(len(total), len(bpe_tokens))
            inserted = ' '.join(total)
            tgt.write(inserted+'\n')

            # print(bpe_tokens)
            # print(token)

if __name__ == "__main__":
    main()