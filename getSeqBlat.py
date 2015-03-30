#!/usr/bin/env python

#
# getSeqBlat.py
#
# author: Joseph Tran <Joseph.Tran@versailles.inra.fr>
# date: 25-03-2015
#

import argparse
import logging

## arguments ##
parser = argparse.ArgumentParser(description="Extract genomic sequences from a blat result")

parser.add_argument("genome", help="genome in fasta format")
parser.add_argument("modblat", help="modified blat alignment file in psl-like format: cf. QT")

parser.add_argument("-t", "--target_transcript_fragment_size", dest="tt_frag_sz", type=int, default=4000, help="the target transcript fragment size to extract [default: %(default)s]")

args = parser.parse_args()

## logging ##
# create logger
logger = logging.getLogger('getSeqBlat')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


## functions ##


### MAIN ###
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

    from getSeqBlatLib import ModBlatHit

    ### steps ###
    ## load genome
    ## load mod blat
    ## iterate over blat hits and extract genomic sequences regarding the given fragment sizes (transcript and LTR) at the reference position
    ### 2 cases: strand + or -
    ## export fasta output
    ### seq_id: Qname ; Tname ; LTR size; transcript size ; total size
    ### seq

    ## load genome
    fasta = args.genome
    logger.debug(fasta)

    ## load mod blat
    logger.debug(args.modblat)

