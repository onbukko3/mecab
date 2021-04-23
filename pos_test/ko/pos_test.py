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

with open(args.src , 'r') as src, open(args.bpe, 'r') as bpe:
    src_token = []
    bpe_token = []

    for src_line, bpe_line in zip(src.readlines(), bpe.readlines()):
        if len(src_line) != len(bpe_line):
            # ori_tags = [pos[1] for pos in mecab.pos(src_line.replace(' ','').replace('▃', ' '))]
            # morph_tag = [pos[1] for pos in mecab.pos(src_line.replace('▃ ', ''))]
            src_tags = [pos[1] for pos in mecab.pos(src_line)]
            bpe_tags = [pos[1] for pos in mecab.pos(bpe_line.replace('@@',''))]
            b_token = bpe_line.split(' ')
            print(src_line)
            print(mecab.pos(src_line))
            print(bpe_line)
            print(mecab.pos(bpe_line))
            print("------------{}-------{}-----{}--".format(len(src_tags), len(bpe_tags), len(b_token)))