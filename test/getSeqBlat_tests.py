#!/usr/bin/env python

# getSeqBlat_tests.py
#
# author: Joseph Tran <Joseph.Tran@versailles.inra.fr>
# date: 30-03-2015
#

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from getSeqBlatLib import ModBlatHit

### test functions ###

def setup_func():
    ''' set up test fixtures
	'''

def teardown_func():
    ''' tear down test fixtures
	'''

# when test a function
#@with_setup(setup_func, teardown_func)


### test classes ###

def TestParseModBlatHit():
    ''' parse modblat hit test
	'''
	
    @classmethod
    def setup_class(cls):
        ''' This method is run once for each class before  any tests  are run 
        '''
        modblat = "../data/BLAT_BX_contigs_Tnt1.txt"

    @classmethod
    def teardown_class(cls):
        ''' This method is run once for each class _after_ all tests are run
        '''

    def setUp(self):
        ''' This method is run once before _each_ test method is run
        '''

    def tearDown(self):
        ''' This method is run once after _each_ test method is run
        '''

    def test_init(self):
        fp = open(modblat)
        with fp as f:
            # skip header line
            next(f)
            for line in f:
                hit = ModBlatHit(line)
                assert_equal(hit.matches, 688)
                break # test only first hit

