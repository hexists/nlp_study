#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import sys
import math


def get_tf(doc_term, term, doc_id):
    if term not in doc_term[doc_id]:
        return 0
    else:
        return doc_term[doc_id][term] / float(len(doc_term[doc_id]))


def get_idf(term_doc, term, all_doc):
    if term not in term_doc:
        return 1.0 
    else:
        return 1.0 + math.log10(all_doc / len(term_doc[term]))


def get_tf_idf(doc_term, term_doc, doc_id, term):
    return get_tf(doc_term, term, doc_id) * get_idf(term_doc, term, float(len(doc_term.keys())))


def calc_cosine_similarity(doc_term, term_doc, doc1, doc2):
    def get_dot_product(vec1, vec2):
        ret = 0.0
        for i in range(len(vec1)):
            ret += vec1[i] * vec2[i]
        return ret

    def get_sqrt_sum(vec):
        ret = 0.0
        for v in vec:
            ret += v * v
        return math.sqrt(ret)


    vec1, vec2 = [], []
    for term in term_doc.keys():
        vec1.append(get_tf_idf(doc_term, term_doc, doc1, term))
        vec2.append(get_tf_idf(doc_term, term_doc, doc2, term))
    dot_product = get_dot_product(vec1, vec2)
    sqrt1 = get_sqrt_sum(vec1)
    sqrt2 = get_sqrt_sum(vec2)
    return dot_product / sqrt1 * sqrt2
    

def main(argv):
    '''
    https://www.hackerrank.com/challenges/nlp-similarity-scores
    http://dev.youngkyu.kr/25
    https://janav.wordpress.com/2013/10/27/tf-idf-and-cosine-similarity/
    http://ra2kstar.tistory.com/86

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
    '''
    for doc_id, terms in doc_term.items():
        for term, freq in terms.items():
            print doc_id, term, freq

    print get_tf(doc_term, 'apple', 2)
    print get_idf(term_doc, 'apple', float(len(docs.keys())))
    '''

    max_doc_id, sim = -1, 0.0
    for doc_id in range(2, len(docs.keys())):
        if sim <= calc_cosine_similarity(doc_term, term_doc, 1, doc_id):
            max_doc_id = doc_id
    print max_doc_id


if __name__ == "__main__":
    main(sys.argv[1:])
