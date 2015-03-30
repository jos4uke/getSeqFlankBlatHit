#!/usr/bin/env python

# getSeqBlat_tests.py
#
# author: Joseph Tran <Joseph.Tran@versailles.inra.fr>
# date: 30-03-2015
#

#import sys
#from os import path
#sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from ..getSeqBlatLib import ModBlatHit

### test functions ###

#def setup_func():
#    ''' set up test fixtures
#    '''
#    pass

#def teardown_func():
#    ''' tear down test fixtures
#    '''
#    pass

# when test a function
#@with_setup(setup_func, teardown_func)


### test classes ###

class TestModBlatHit():
    @classmethod
    def setup_class(cls):
        ''' This method is run once for each class before  any tests  are run 
        '''

    @classmethod
    def teardown_class(cls):
        ''' This method is run once for each class _after_ all tests are run
        '''

    def setUp(self):
        ''' This method is run once before _each_ test method is run
        '''
        self.modblat = "../data/BLAT_BX_contigs_Tnt1.txt"

    def tearDown(self):
        ''' This method is run once after _each_ test method is run
        '''

    def test_init(self):
        fp = open(self.modblat)
        with fp as f:
            # skip header line
            next(f)
            for line in f:
                hit = ModBlatHit(line)
                print hit.matches
                # test only first hit
                assert hit.matches == 688
                assert hit.mismatches == 2
                assert hit.repmatches == 0
                assert hit.countN == 0
                assert hit.qgapcount == 0
                assert hit.qgapbases == 0
                assert hit.tgapcount == 1
                assert hit.tgapbases == 1
                assert hit.strand == "-"
                assert hit.qname == "mira_c2413"
                assert hit.qsize == 1713
                assert hit.qstart == 0
                assert hit.textractsize == 615
                assert hit.qend == 690
                assert hit.tname == "gb|AWOK01517809.1|"
                assert hit.tsize == 3304
                assert hit.tstart == 0
                assert hit.tend == 691
                assert hit.blockcount == 2
                assert hit.blocksizes == [517,173]
                assert hit.qstarts == [1023,1540]
                assert hit.tstarts == [0,518]
                break # end test only first hit

