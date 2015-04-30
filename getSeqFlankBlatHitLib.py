#!/usr/bin/env python

import math

## functions ##


## classes ##

class GenomicDirections():
    ''' Class to represent genomic directions
    '''
    UPSTREAM="upstream"
    DOWNSTREAM="downstream"

class ModBlatHit(object):
    ''' Class for the modified blat/psl format alignment hit (cf. QT).
        Argument: String in modblat format
    '''

    def __init__(self, s):

        # split and tokenize input
        fields = s.strip().split()
        numFields = len(fields)
        matches, mismatches, repmatches, countN, qgapcount, qgapbases, \
            tgapcount, tgapbases, strand, qname, qsize, qstart,	qend, \
            tname, tsize, tstart, tend, blockcount, blocksizes, qstarts, \
            tstarts = fields[0:21]

        self.matches = int(matches)
        self.mismatches = int(mismatches)
        self.repmatches = int(repmatches)
        self.countN = int(countN)
        self.qgapcount = int(qgapcount)
        self.qgapbases = int(qgapbases)
        self.tgapcount = int(tgapcount)
        self.tgapbases = int(tgapbases)
        self.strand = strand
        self.qname = qname
        self.qsize = int(qsize)
        self.qstart = int(qstart)
        self.qend = int(qend)
        self.tname = tname
        self.tsize = int(tsize)
        self.tstart = int(tstart)
        self.tend = int(tend)
        self.blockcount = int(blockcount)
        self.blocksizes = [int(x) for x in blocksizes.split(',')[0:-1]]
        self.qstarts = [int(x) for x in qstarts.split(',')[0:-1]]
        self.tstarts = [int(x) for x in tstarts.strip().split(',')[0:-1]]

    def computeGenomicSequenceBedItem(self, ltr_size, transcript_size):
        ''' compute start, end by strand
            set and return bed item
        '''
        if self.strand == '+':
            chrom = self.tname
            chromStart = self.computeGenomicSequenceCoord(ltr_size, self.tstart, 'upstream')
            chromEnd = self.computeGenomicSequenceCoord(transcript_size, self.tstart, 'downstream')
            length = chromEnd - chromStart + 1
            score = 0
            strand = '+'
            bi = BedItem([chrom, chromStart, chromEnd])
            name = " ; ".join([self.qname, self.tname, str(bi.chromStart) + ":" + str(bi.chromEnd), str(length)])
            bi.set_name(name)
            bi.set_score(score)
            bi.set_strand(strand)
            return bi
        elif self.strand == '-':
            chrom = self.tname
            chromStart = self.computeGenomicSequenceCoord(transcript_size, self.tend, 'upstream')
            chromEnd = self.computeGenomicSequenceCoord(ltr_size, self.tend, 'downstream')
            length = chromEnd - chromStart + 1
            score = 0
            strand = '-'
            bi = BedItem([chrom, chromStart, chromEnd])
            name = " ; ".join([self.qname, self.tname, str(bi.chromStart) + ":" + str(bi.chromEnd), str(length), 'rc'])
            bi.set_name(name)
            bi.set_score(score)
            bi.set_strand(strand)
            return bi
        else:
            pass

    def computeGenomicSequenceCoord(self, frag_size, ref_position, genomic_direction):
        ''' compute genomic sequence coordinate given the genomic fragment size to extract, the reference position to start from
            and the direction
        '''
        assert genomic_direction in set([GenomicDirections.UPSTREAM, GenomicDirections.DOWNSTREAM])

        if genomic_direction == GenomicDirections.UPSTREAM:
            target_upstream_length = ref_position
            if target_upstream_length > frag_size:
                genomicCoord = ref_position - frag_size
            else:
                genomicCoord = 0

        elif genomic_direction == GenomicDirections.DOWNSTREAM:
            target_downstream_length = self.tsize - ref_position
            if target_downstream_length > frag_size:
                genomicCoord = ref_position + frag_size
            else:
                genomicCoord = self.tsize - 1 

        return genomicCoord
        


class ModBlat(object):
    ''' Class for representing the modified blat/psl file alignments.
        Argument: String to modblat file
    '''

    def __init__(self, s):
        self.filename = s
        self.hits = self.__load()
        
    def __load(self):
        modblathits = []
        fp = open(self.filename)
        with fp as f:
            # skip header line
            next(f)
            for line in f:
                hit = ModBlatHit(line)
                modblathits.append(hit)
        
        return modblathits


class BedItem():
    ''' Class for representing a bed item
    '''

    def __init__(self, a):
        chrom, chromStart, chromEnd = a[0:3]

        self.chrom = chrom
        if int(chromStart) == 0:
            self.chromStart = int(chromStart)    
        else:
            self.chromStart = int(chromStart) - 1
        if int(chromEnd) == 0:
            self.chromEnd = int(chromEnd)
        else:
            self.chromEnd = int(chromEnd) - 1

    def set_name(self, s):
        self.name = s

    def set_score(self, i):
        self.score = int(i)

    def set_strand(self, s):
        self.strand = s

    def totuple(self):
        t = (self.chrom,
                self.chromStart,
                self.chromEnd,
                self.name,
                self.score,
                self.strand)
        return t
