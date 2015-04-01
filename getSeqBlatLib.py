#!/usr/bin/env python

import math

## classes ##
class ModBlatHit(object):
    ''' Class for the modified blat/psl format alignment hit (cf. QT).
        Argument: String in modblat format
    '''

    def __init__(self, s):

        # split and tokenize input
        fields = s.strip().split()
        numFields = len(fields)
        matches, mismatches, repmatches, countN, qgapcount, qgapbases, \
            tgapcount, tgapbases, strand, qname, qsize, qstart,	textractsize, qend, \
            tname, tsize, tstart, tend, blockcount, blocksizes, qstarts, \
            tstarts = fields[0:22]

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
        self.textractsize = int(textractsize)
        self.qend = int(qend)
        self.tname = tname
        self.tsize = int(tsize)
        self.tstart = int(tstart)
        self.tend = int(tend)
        self.blockcount = int(blockcount)
        self.blocksizes = [int(x) for x in blocksizes.split(',')[0:-1]]
        self.qstarts = [int(x) for x in qstarts.split(',')[0:-1]]
        self.tstarts = [int(x) for x in tstarts.strip().split(',')[0:-1]]
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

