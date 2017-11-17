https://machinelearningmastery.com/develop-word-embedding-model-predicting-movie-review-sentiment/?utm_content=buffer007bc&utm_medium=social&utm_source=linkedin.com&utm_campaign=buffer

2017.11.17. SA tutorial

+ 로컬에서 테스트

1) dataset 다운로드
```
wget http://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz
tar xvzf review_polarity.tar.gz
```

2) training, test 데이터 구분
```
0~8xx : training
9xx   : test

3) virtualenv 세팅
$ virturalenv SA
$ source SA/bin/activate
$ pip install nltk
$ python
  >>> import nltk
  >>> nltk.download('stopwords')
$ pip install tensorflow
$ pip install keras
$ pip install Gensim
```

4) cleansing
```
+ 데이터가 워낙 깨끗해서 아주 간단한 처리만 진행
+ 잘못 작성된 코드 수정
https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
# remove punctuation from each token
tokens = [w.translate(None, string.punctuation) for w in tokens]
```

5) voca
```
+ Counter를 사용해서 개발되어 있음
+ min_occur=2 보다 큰 것만 필터링해서 vocab.txt로 저장
```

6) Train Embedding Layer
```
+ Keras deep learning library using the Embedding layer를 사용
+ Tokenizer()를 통해 sequences of integers로 변환
+ max length를 계산한 뒤, max length가 아닌 경우는 0으로 패딩
+ input size(embedding size): maximum length of input doc
+ voca size : all words + unknown word
+ 100-dimensional vector space
+ CNN으로 ...
+ 32 filters, kernel size of 8, relu + polling layer
+ 2D flatten X MLP
+ binary cross entropy loss function 사용

+ 실행 결과
Using TensorFlow backend.
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
embedding_1 (Embedding)      (None, 1317, 100)         2576800
_________________________________________________________________
conv1d_1 (Conv1D)            (None, 1310, 32)          25632
_________________________________________________________________
max_pooling1d_1 (MaxPooling1 (None, 655, 32)           0
_________________________________________________________________
flatten_1 (Flatten)          (None, 20960)             0
_________________________________________________________________
dense_1 (Dense)              (None, 10)                209610
_________________________________________________________________
dense_2 (Dense)              (None, 1)                 11
=================================================================
Total params: 2,812,053
Trainable params: 2,812,053
Non-trainable params: 0
_________________________________________________________________
None
Epoch 1/10
 - 18s - loss: 0.6875 - acc: 0.5356
Epoch 2/10
 - 21s - loss: 0.5614 - acc: 0.7200
Epoch 3/10
 - 18s - loss: 0.3813 - acc: 0.9428
Epoch 4/10
 - 18s - loss: 0.3220 - acc: 0.9811
Epoch 5/10
 - 18s - loss: 0.3018 - acc: 0.9850
Epoch 6/10
 - 17s - loss: 0.2862 - acc: 0.9883
Epoch 7/10
 - 17s - loss: 0.2739 - acc: 0.9883
Epoch 8/10
 - 17s - loss: 0.2627 - acc: 0.9883
Epoch 9/10
 - 20s - loss: 0.2518 - acc: 0.9889
Epoch 10/10
 - 20s - loss: 0.2419 - acc: 0.9889
Test Accuracy: 86.000000
```

7) word2vec
```
+ sentence 정보 유지
+ Gensim 써서 word2vec 계산

+ 실행 결과
25767 100
film 0.030162 0.278404 -1.379401 -0.936823 0.379066 -0.385098 0.324767 1.013149 -0.204541 -0.031200 -0.272795 -0.138861 -0.082377 -0.328233 -0.482671 0.215348 -0.632877 -0.621891 -0.305300 -0.740641 -1.184498 -0.529811 0.376099 -0.389485 0.735164 0.432667 -0.524383 0.059199 -0.064224 -2.280695 -0.212285 0.358962 -0.029500 0.240921 -0.637735 0.723263 -0.578901 0.076326 0.212414 -0.238136 -0.707425 -0.043100 -0.272518 -0.258888 -0.717345 -0.528443 0.442722 -0.556261 0.166018 0.647280 -0.416529 -1.019019 -0.152869 -0.284187 -0.248091 -0.230512 -0.530631 0.262351 -0.462858 0.075526 0.639857 -0.168790 0.588066 -0.264950 0.208927 -0.323763 -0.273928 -1.098281 0.582148 -0.565156 0.688234 -1.059754 -0.207217 0.100320 0.543611 -1.008824 -0.318633 -0.873960 1.293576 -0.248162 0.306654 0.281288 0.066070 -0.369840 -0.405289 0.179471 0.079823 -0.469338 -0.876167 0.463088 -0.849297 -0.284970 0.069412 -0.767920 -0.603286 0.066781 0.250099 -0.761576 -0.366838 0.311921
```

8) w2v 사용
```
+ 실행 결과
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
embedding_1 (Embedding)      (None, 1317, 100)         2576800
_________________________________________________________________
conv1d_1 (Conv1D)            (None, 1313, 128)         64128
_________________________________________________________________
max_pooling1d_1 (MaxPooling1 (None, 656, 128)          0
_________________________________________________________________
flatten_1 (Flatten)          (None, 83968)             0
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 83969
=================================================================
Total params: 2,724,897
Trainable params: 148,097
Non-trainable params: 2,576,800
_________________________________________________________________
None
Epoch 1/10
 - 23s - loss: 0.7075 - acc: 0.5278
Epoch 2/10
 - 20s - loss: 0.6556 - acc: 0.6156
Epoch 3/10
 - 23s - loss: 0.5652 - acc: 0.7128
Epoch 4/10
 - 25s - loss: 0.4691 - acc: 0.7800
Epoch 5/10
 - 22s - loss: 0.3469 - acc: 0.8711
Epoch 6/10
 - 21s - loss: 0.2513 - acc: 0.9183
Epoch 7/10
 - 21s - loss: 0.1689 - acc: 0.9506
Epoch 8/10
 - 21s - loss: 0.1072 - acc: 0.9828
Epoch 9/10
 - 20s - loss: 0.0663 - acc: 0.9933
Epoch 10/10
 - 21s - loss: 0.0430 - acc: 0.9994
Test Accuracy: 56.000000

+ 성능이 떨어지는데, w2c conf 또는 nn conf 때문일 수 있음

+ trainable=True로 바꿔서 테스트 => 약간 오르지만 성능이 떨어짐(나는 더 떨어짐)
Test Accuracy: 63.500000

+ layer 10, relu 추가 후
Test Accuracy: 68.500000

+ google, stanford wv 사용해서 해볼수도 있음

+ pre-trained GloVe vector from stanford(wiki)
http://nlp.stanford.edu/data/glove.6B.zip
Test Accuracy: 73.500000

+ trainable=True
Test Accuracy: 82.000000

+ layer 10, relu 추가 후 
Test Accuracy: 80.500000
```

9) 정리 후 commit
```
pip freeze > requirements.txt
git commit
```
