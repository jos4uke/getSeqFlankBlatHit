#!/usr/bin/env python

#
# getSeqBlat.py
#
# author: Joseph Tran <Joseph.Tran@versailles.inra.fr>
# date: 25-03-2015
#

import argparse

## parse arguments
parser = argparse.ArgumentParser(description="Extract genomic sequences from a blat result")

parser.add_argument("genome", help="genome in fasta format")
parser.add_argument("modblat", help="modified blat alignment file in psl-like format: cf. QT")

parser.add_argument("-t", "--target_transcript_fragment_size", dest="tt_frag_sz", type=int, default=4000, help="the target transcript fragment size to extract [default: %(default)s]")

args = parser.parse_args()

## load genome
## load blat
## iterate over blat hits and extract genomic sequences regarding the given fragment sizes (transcript and LTR) at the reference position
### 2 cases: strand + or -
