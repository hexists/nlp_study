#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import sys
from collections import Counter


def main(argv):
    '''
    https://www.hackerrank.com/challenges/nlp-pos-tagging

    input:
    The/DT planet/NN Jupiter/NNP and/CC its/PPS moons/NNS are/VBP in/IN effect/NN a/DT minisolar/JJ system/?? ,/, and/CC Jupiter/NNP itself/PRP is/VBZ often/RB called/VBN a/DT star/?? that/IN never/RB caught/??? fire/NN ./.
    '''

    tagged_sen = '''The/DT planet/NN Jupiter/NNP and/CC its/PPS moons/NNS are/VBP in/IN effect/NN a/DT minisolar/JJ system/?? ,/, and/CC Jupiter/NNP itself/PRP is/VBZ often/RB called/VBN a/DT star/?? that/IN never/RB caught/??? fire/NN ./.'''

    tag2, tag3 = Counter(), Counter()
    for word_tag in tagged_sen.split():
        idx = word_tag.rfind('/')
        word, tag = word_tag[:idx], word_tag[idx + 1:]
        if len(tag) == 3 and tag != '???':
            tag3[tag] += 1
        elif len(tag) == 2 and tag != '??':
            tag2[tag] += 1

    tag3_most = tag3.most_common(1)[0][0]
    tag2_most = tag2.most_common(1)[0][0]

    print tagged_sen.replace('???', tag3_most).replace('??', tag2_most)

if __name__ == "__main__":
    main(sys.argv[1:])
