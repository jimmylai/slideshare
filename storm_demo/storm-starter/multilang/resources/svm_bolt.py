#!/usr/bin/env python
# -*- encoding: utf8 -*-

import json
import cPickle as pkl
import storm
import traceback
from numpy import array

__author__ = 'noahsark'


class SVMBolt(storm.BasicBolt):
    def initialize(self, stormconf, context):
        '''initialize your members here.'''
        try:
            self.model = pkl.load(open('svm_model.pkl', 'rb'))
        except:
            traceback.print_exc(file=open('/tmp/trace_svm_bolt.txt', 'a'))

    def process(self, tup):
        '''We serialize the input and output by json for convenience.'''
        try:
            data = array(json.loads(tup.values[1]))
            result = self.model.predict(data)
            storm.emit([tup.values[0], json.dumps(result.tolist())])
        except:
            traceback.print_exc(file=open('/tmp/trace_svm_bolt.txt', 'a'))

if __name__ == '__main__':
    try:
        SVMBolt().run()
    except:
        traceback.print_exc(file=open('/tmp/trace_svm_bolt.txt', 'a'))
