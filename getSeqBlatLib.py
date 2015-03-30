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


