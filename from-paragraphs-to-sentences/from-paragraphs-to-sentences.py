#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import sys


def main(argv):
    '''
    https://www.hackerrank.com/challenges/from-paragraphs-to-sentences
    '''
    end_symbol = ['.', '?', '!', '\n']
    quote_symbol = ['"']

    buf = raw_input()
    line, qflag = '', False
    for ch in buf:
        line += ch
        if qflag is False and ch in end_symbol:
            print line.strip()
            line = ''
        if ch in quote_symbol:
            qflag = not qflag


if __name__ == "__main__":
    main(sys.argv[1:])
