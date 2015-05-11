#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Program
'''

from thrift import Thrift
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket, TTransport
from storm import DistributedRPC
from storm.ttypes import DRPCExecutionException
from sklearn import datasets, metrics
from numpy import array
import json


__author__ = 'noahsark'


class Client(DistributedRPC.Iface):
    def __init__(self, host='localhost', port=3772, timeout=6000):
        try:
            socket = TSocket.TSocket(host, port)
            socket.setTimeout(timeout)
            self.conn = TTransport.TFramedTransport(socket)
            self.client = DistributedRPC.Client(TBinaryProtocol.TBinaryProtocol(self.conn))
            self.conn.open()
        except Thrift.TException, exc:
            print exc

    def close(self):
        self.conn.close()

    def execute(self, func, args):
        try:
            return self.client.execute(func, args)
        except Thrift.TException, exc:
            print exc.message()
        except DRPCExecutionException, exc:
            print exc

if __name__ == '__main__':
    '''send 10 data to server for prediction.'''
    client = Client()
    test = datasets.fetch_20newsgroups_vectorized(subset='test')
    data_size = 40
    input_json = json.dumps(test.data[:data_size].toarray().tolist())
    print 'data prepared'
    result = client.execute('svm', input_json)
    print 'data predicted'
    result = array(json.loads(result))
    print metrics.classification_report(test.target[:data_size], result)
    client.close()
