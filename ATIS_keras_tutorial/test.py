#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import numpy as np
import data.load

train_set, valid_set, dicts = data.load.atisfull()
w2idx, labels2idx = dicts['words2idx'], dicts['labels2idx']

# Q. 여기서 _에도 정보가 담겨있는데, 왜 안 쓰는지 잘 모르겠음
train_x, _, train_label = train_set
val_x, _, val_label = valid_set

# Create index to word/label dicts, Q. 왜 이렇게 역으로 dict를 만들지?
idx2w = {w2idx[k]: k for k in w2idx}
idx2la = {labels2idx[k]: k for k in labels2idx}

# For conlleval script <= 확인을 위해 converting 해서 두는 듯...
words_train = [list(map(lambda x: idx2w[x], w)) for w in train_x]
labels_train = [list(map(lambda x: idx2la[x], y)) for y in train_label]
words_val = [list(map(lambda x: idx2w[x], w)) for w in val_x]
labels_val = [list(map(lambda x: idx2la[x], y)) for y in val_label]

n_classes = len(idx2la)
n_vocab = len(idx2w)

print("Example sentence : {}".format(words_train[0]))
print("Encoded form: {}".format(train_x[0]))
print()
print("It's label : {}".format(labels_train[0]))
print("Encoded form: {}".format(train_label[0]))

from keras.models import Sequential
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import SimpleRNN
from keras.layers.core import Dense, Dropout
from keras.layers.wrappers import TimeDistributed
from keras.layers import Convolution1D

model = Sequential()
# https://keras.io/layers/embeddings/#embedding
# keras.layers.Embedding(input_dim, output_dim, embeddings_initializer='uniform', embeddings_regularizer=None, activity_regularizer=None, embeddings_constraint=None, mask_zero=False, input_length=None)
model.add(Embedding(n_vocab, 100))
model.add(Dropout(0.25))
# https://keras.io/layers/recurrent/#simplernn
# keras.layers.SimpleRNN(units, activation='tanh', use_bias=True, kernel_initializer='glorot_uniform', recurrent_initializer='orthogonal', bias_initializer='zeros', kernel_regularizer=None, recurrent_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, recurrent_constraint=None, bias_constraint=None, dropout=0.0, recurrent_dropout=0.0, return_sequences=False, return_state=False, go_backwards=False, stateful=False, unroll=False)
# units: Positive integer, dimensionality of the output space.
# return_sequences: Boolean. Whether to return the last output. in the output sequence, or the full sequence.
model.add(SimpleRNN(100, return_sequences=True))
# https://keras.io/layers/wrappers/#timedistributed
# This wrapper applies a layer to every temporal slice of an input.
# Q. ouput shape (n_classes, n_vocab, n_classes) 이게 맞나?
model.add(TimeDistributed(Dense(n_classes, activation='softmax')))
model.compile('rmsprop', 'categorical_crossentropy')

import progressbar
n_epochs = 30

for i in range(n_epochs):
    print("Training epoch {}".format(i))
    bar = progressbar.ProgressBar(max_value=len(train_x))
    for n_batch, sent in bar(enumerate(train_x)):
        label = train_label[n_batch]
        # Make labels one hot
        label = np.eye(n_classes)[label][np.newaxis,:]
        # View each sentence as a batch
        sent = sent[np.newaxis,:]

        if sent.shape[1] > 1:  # ignore 1 word sentences
            model.train_on_batch(sent, label)


from metrics.accuracy import conlleval

labels_pred_val = []

bar = progressbar.ProgressBar(max_value=len(val_x))
for n_batch, sent in bar(enumerate(val_x)):
    label = val_label[n_batch]
    label = np.eye(n_classes)[label][np.newaxis,:]
    sent = sent[np.newaxis,:]

    pred = model.predict_on_batch(sent)
    pred = np.argmax(pred,-1)[0]
    labels_pred_val.append(pred)

labels_pred_val = [list(map(lambda x: idx2la[x], y)) for y in labels_pred_val]
con_dict = conlleval(labels_pred_val, labels_val, words_val, 'measure.txt')

print('Precision = {}, Recall = {}, F1 = {}'.format(con_dict['r'], con_dict['p'], con_dict['f1']))
