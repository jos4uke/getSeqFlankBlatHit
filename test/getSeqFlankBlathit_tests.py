#!/usr/bin/env python

# getSeqFlankBlatHit_tests.py
#
# author: Joseph Tran <Joseph.Tran@versailles.inra.fr>
# date: 30-03-2015
#

#import sys
#from os import path
#sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from ..getSeqFlankBlatHitLib import ModBlatHit, ModBlat, BedItem

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

    def test_computeGenomicSequenceStart_forward_longupstream(self):
        # test genomic sequence start computation for forward strand hit 
        # and when upstream sequence is longer than the fragment size to extract
        
        hitline = "1408	0	0	0	2	2	2	2	+	mira_c1293	1410	0	1410	gb|AWOK01488203.1|	41178	36524	37934	5	941,13,243,204,7,	0,941,955,1199,1403,	36524,37466,37479,37722,37927,"
        frag_size = 615
        chromStart_exp = 36524 - frag_size
        hit = ModBlatHit(hitline)
        chromStart_comp = hit.computeGenomicSequenceCoord(frag_size, hit.tstart, 'upstream')
        assert chromStart_comp == chromStart_exp

    def test_computeGenomicSequenceStart_forward_shortupstream(self):
        # test genomic sequence start computation for forward strand hit 
        # and when upstream sequence is shorter than the fragment size to extract
        
        hitline = "1408	0	0	0	2	2	2	2	+	mira_c1293	1410	0	1410	gb|AWOK01488203.1|	41178	36524	37934	5	941,13,243,204,7,	0,941,955,1199,1403,	36524,37466,37479,37722,37927,"
        hit = ModBlatHit(hitline)
        chromStart_exp = 0
        
        print "Zero case"
        frag_size = 36524
        chromStart_comp = hit.computeGenomicSequenceCoord(frag_size, hit.tstart, 'upstream')
        assert chromStart_comp == chromStart_exp

        print "Shorter case"
        frag_size = 41178
        chromStart_comp = hit.computeGenomicSequenceCoord(frag_size, hit.tstart, 'upstream')
        assert chromStart_comp == chromStart_exp

    def test_computeGenomicSequenceStart_reverse_longupstream(self):
        # test genomic sequence start computation for reverse strand hit 
        # and when upstream sequence is longer than the fragment size to extract
        
        hitline = "359	2	0	0	1	5	1	1	-	mira_rep_c5792	366	0	366	gb|AWOK01096782.1|	49796	48388	48750	2	7,354,	0,12,	48388,48396," 
        frag_size = 4000
        chromStart_exp = 48750 - frag_size
        hit = ModBlatHit(hitline)
        chromStart_comp = hit.computeGenomicSequenceCoord(frag_size, hit.tend, 'upstream')
        assert chromStart_comp == chromStart_exp

    def test_computeGenomicSequenceStart_reverse_shortupstream(self):
        # test genomic sequence start computation for forward strand hit 
        # and when upstream sequence is shorter than the fragment size to extract
        
        hitline = "359	2	0	0	1	5	1	1	-	mira_rep_c5792	366	0	366	gb|AWOK01096782.1|	49796	48388	48750	2	7,354,	0,12,	48388,48396," 
        chromStart_exp = 0
        hit = ModBlatHit(hitline)

        print "Zero case"
        frag_size = 48750       
        chromStart_comp = hit.computeGenomicSequenceCoord(frag_size, hit.tend, 'upstream')
        print chromStart_comp
        assert chromStart_comp == chromStart_exp

        print "Shorter case"
        frag_size = 49796        
        chromStart_comp = hit.computeGenomicSequenceCoord(frag_size, hit.tend, 'upstream')
        assert chromStart_comp == chromStart_exp

    def test_computeGenomicSequenceEnd_forward_longdownstream(self):
        # test genomic sequence end computation for forward strand hit 
        # and when downstream sequence is longer than the fragment size to extract
        
        hitline="2349	2	0	0	2	2	3	122	+	mira_c148	2353	0	2353	gb|AWOK01318317.1|	18255	5826	8299	6	46,322,748,78,1007,150,	0,46,369,1117,1196,2203,	5826,5873,6195,7063,7141,8149,"
        frag_size = 4000
        chromEnd_exp = 5826 + frag_size
        hit = ModBlatHit(hitline)
        chromEnd_comp = hit.computeGenomicSequenceCoord(frag_size, hit.tstart, 'downstream')
        assert chromEnd_comp == chromEnd_exp

    def test_computeGenomicSequenceEnd_forward_shortdownstream(self):
        # test genomic sequence end computation for forward strand hit 
        # and when downstream sequence is shorter than the fragment size to extract
        
        hitline="2349	2	0	0	2	2	3	122	+	mira_c148	2353	0	2353	gb|AWOK01318317.1|	18255	5826	8299	6	46,322,748,78,1007,150,	0,46,369,1117,1196,2203,	5826,5873,6195,7063,7141,8149,"
        chromEnd_exp = 18254
        hit = ModBlatHit(hitline)

        print "Zero case"
        frag_size = 12429
        chromEnd_comp = hit.computeGenomicSequenceCoord(frag_size, hit.tstart, 'downstream')
        print 
        assert chromEnd_comp == chromEnd_exp

    def test_computeGenomicSequenceEnd_reverse_longdownstream(self):
        # test genomic sequence end computation for reverse strand hit 
        # and when downstream sequence is longer than the fragment size to extract
        
        hitline = "359	2	0	0	1	5	1	1	-	mira_rep_c5792	366	0	366	gb|AWOK01096782.1|	49796	48388	48750	2	7,354,	0,12,	48388,48396," 
        frag_size = 615
        chromEnd_exp = 48750 + frag_size
        hit = ModBlatHit(hitline)
        chromEnd_comp = hit.computeGenomicSequenceCoord(frag_size, hit.tend, 'downstream')
        assert chromEnd_comp == chromEnd_exp

    def test_computeGenomicSequenceEnd_reverse_shortdownstream(self):
        # test genomic sequence end computation for reverse strand hit 
        # and when downstream sequence is shorter than the fragment size to extract
        
        hitline = "359	2	0	0	1	5	1	1	-	mira_rep_c5792	366	0	366	gb|AWOK01096782.1|	49796	48388	48750	2	7,354,	0,12,	48388,48396,"
        chromEnd_exp = 49796 - 1
        hit = ModBlatHit(hitline)
        
        print "Zero case"
        frag_size = 1046
        chromEnd_comp = hit.computeGenomicSequenceCoord(frag_size, hit.tend, 'downstream')
        assert chromEnd_comp == chromEnd_exp

        print "Shorter case"
        frag_size = 1500
        chromEnd_comp = hit.computeGenomicSequenceCoord(frag_size, hit.tend, 'downstream')
        assert chromEnd_comp == chromEnd_exp

    def test_computeGenomicSequenceCoord_forward(self):
        # test genomic sequence bed item computation for a forward strand hit

        hitline="2349	2	0	0	2	2	3	122	+	mira_c148	2353	0	2353	gb|AWOK01318317.1|	18255	5826	8299	6	46,322,748,78,1007,150,	0,46,369,1117,1196,2203,	5826,5873,6195,7063,7141,8149,"
        ltr_size = 615
        transcript_size = 4000
        hit = ModBlatHit(hitline)
        bi = hit.computeGenomicSequenceBedItem(ltr_size, transcript_size)
        t_comp = bi.totuple()
        chrom_exp = 'gb|AWOK01318317.1|'
        chromStart_exp = 5826 - ltr_size
        chromEnd_exp = 5826 + transcript_size
        length = chromEnd_exp - chromStart_exp + 1
        name_exp = " ; ".join(['mira_c148', 'gb|AWOK01318317.1|', str(chromStart_exp) + ":" + str(chromEnd_exp), str(length)]) 
        t_exp = (chrom_exp,
                    chromStart_exp,
                    chromEnd_exp,
                    name_exp,
                    0,
                    'forward')
        assert t_comp == t_exp
    
    def test_computeGenomicSequenceCoord_reverse(self):
        # test genomic sequence bed item computation for a reverse strand hit

        hitline = "359	2	0	0	1	5	1	1	-	mira_rep_c5792	366	0	366	gb|AWOK01096782.1|	49796	48388	48750	2	7,354,	0,12,	48388,48396,"
        ltr_size = 615
        transcript_size = 4000
        hit = ModBlatHit(hitline)
        bi = hit.computeGenomicSequenceBedItem(ltr_size, transcript_size)
        t_comp = bi.totuple()
        chrom_exp = 'gb|AWOK01096782.1|'
        chromStart_exp = 48750 - transcript_size
        chromEnd_exp = 48750 + ltr_size
        length = chromEnd_exp - chromStart_exp + 1
        name_exp = " ; ".join(['mira_rep_c5792', 'gb|AWOK01096782.1|', str(chromStart_exp) + ":" + str(chromEnd_exp), str(length), 'rc']) 
        t_exp = (chrom_exp,
                    chromStart_exp,
                    chromEnd_exp,
                    name_exp,
                    0,
                    'reverse')
        assert t_comp == t_exp


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


