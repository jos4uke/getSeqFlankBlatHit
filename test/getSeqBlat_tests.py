#!/usr/bin/env python

# getSeqBlat_tests.py
#
# author: Joseph Tran <Joseph.Tran@versailles.inra.fr>
# date: 30-03-2015
#

#import sys
#from os import path
#sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from ..getSeqBlatLib import ModBlatHit, ModBlat

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

class TestLoadModBlat():
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
        mb = ModBlat(self.modblat)
        assert mb.filename == self.modblat
        assert len(mb.hits) == 72

class TestBedItem():
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
        self.beditem = ['chr1', 1, 10]
        self.name = 'forward'
        self.score = 0
        self.strand = '+'

    def tearDown(self):
        ''' This method is run once after _each_ test method is run
        '''

    def test_init(self):
        bi = BedItem(self.beditem)
        assert bi.chrom == 'chr1'
        assert bi.chromStart == 1
        assert bi.chromEnd == 10

    def test_name(self):
        bi = BedItem(self.beditem)
        bi.set_name(self.name)
        assert bi.name == self.name

    def test_score(self):
        bi = BedItem(self.beditem)
        bi.set_score(self.score)
        assert bi.score == self.score

    def test_strand(self):
        bi = BedItem(self.beditem)
        bi.set_strand(self.strand)
        assert bi.strand == self.strand

    def test_totuple(self):
        bi = BedItem(self.beditem)
        bi.set_name(self.name)
        bi.set_score(self.score)
        bi.set_strand(self.strand)
        t = (self.beditem[0],
                self.beditem[1],
                self.beditem[2],
                self.name,
                self.score,
                self.strand)        
        assert bi.totuple() == t


