#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Train a svm model using 20newsgroup data.
'''

from sklearn import datasets, svm
import cPickle as pkl


__author__ = 'noahsark'


train = datasets.fetch_20newsgroups_vectorized(subset='train')
clf = svm.LinearSVC()
clf.fit(train.data, train.target)
with open('storm-starter/multilang/resources/svm_model.pkl', 'wb') as fp_:
    pkl.dump(clf, fp_)
