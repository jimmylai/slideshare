#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Test
'''
from nose import with_setup
import nose.tools as nt
from my_operator import adder, divider


__author__ = 'noahsark'


def setup():
    global test_case_1
    test_case_1 = (1, 2)


def teardown():
    pass


@with_setup(setup, teardown)
def test_adder():
    expected = 3
    actual = adder(test_case_1[0], test_case_1[1])
    nt.assert_equal(actual, expected)


@with_setup(setup, teardown)
def test_divider():
    expected = 0.5
    actual = divider(test_case_1[0], test_case_1[1])
    nt.assert_equal(actual, expected)
