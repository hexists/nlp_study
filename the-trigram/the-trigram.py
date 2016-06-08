#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import sys
import operator
import re


def main(argv):
    '''
    https://www.hackerrank.com/challenges/the-trigram
    '''

    reg = re.compile('[.\n]+')

    words = ''
    for buf in sys.stdin:
      words += buf
    words = reg.sub(' ', words).lower().split()

    trigrams = {}
    for i in range(len(words) - 2):
        trigram = ' '.join(words[i:i + 3]).strip()
        if trigram not in trigrams:
          trigrams[trigram] = 1
        else:
          trigrams[trigram] += 1

    print max(trigrams.iteritems(), key=operator.itemgetter(1))[0]


if __name__ == "__main__":
    main(sys.argv[1:])
