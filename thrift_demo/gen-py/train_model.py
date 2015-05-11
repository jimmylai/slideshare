#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Train a svm model using iris model.
'''

from sklearn import datasets, svm
import cPickle as pkl

__author__ = 'noahsark'

digits = datasets.load_digits()
clf = svm.LinearSVC()
size = int(digits.data.shape[0] * 0.8)
clf.fit(digits.data[:size], digits.target[:size])
with open('svm_model.pkl', 'wb') as fp_:
    pkl.dump(clf, fp_)

