#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import sys
import math


def main(argv):
    '''
    https://www.hackerrank.com/challenges/nlp-compute-the-perplexity
    http://bestmike007.com/2011/07/perplexity-cross-entropy/
    '''
    buf = float(raw_input())
    print int(math.pow(2, buf))


if __name__ == "__main__":
    main(sys.argv[1:])
