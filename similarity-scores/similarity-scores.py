#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import sys
import math


def get_tf(doc_term, term, doc_id):
    if term not in doc_term[doc_id]:
        return 0
    else:
        return doc_term[doc_id][term]


def get_idf(term_doc, term, all_doc):
    if term not in term_doc:
        return 0
    else:
        return math.log10(all_doc / len(term_doc[term]))


def main(argv):
    '''
    https://www.hackerrank.com/challenges/nlp-similarity-scores
    http://dev.youngkyu.kr/25
    https://janav.wordpress.com/2013/10/27/tf-idf-and-cosine-similarity/

    input:
    I'd like an apple.
    An apple a day keeps the doctor away.
    Never compare an apple to an orange.
    I prefer scikit-learn to orange.
    '''

    docs = {1: 'I\'d like an apple.',
            2: 'An apple a day keeps the doctor away.',
            3: 'Never compare an apple to an orange.',
            4: 'I prefer scikit-learn to orange.'}

    doc_term = {doc_id: {} for doc_id in docs.keys()}
    term_doc = {}
    for doc_id, words in docs.items():
        for word in words.split():
            if word not in term_doc:
                term_doc[word] = [doc_id]
            else:
                term_doc[word].append(doc_id)

            if word not in doc_term[doc_id]:
                doc_term[doc_id][word] = 1
            else:
                doc_term[doc_id][word] += 1

    for doc_id, terms in doc_term.items():
        for term, freq in terms.items():
            print doc_id, term, freq

    print get_tf(doc_term, 'apple', 2)
    print get_idf(term_doc, 'apple', float(len(docs.keys())))

if __name__ == "__main__":
    main(sys.argv[1:])
