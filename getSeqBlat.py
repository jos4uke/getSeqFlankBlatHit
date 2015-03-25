#!/usr/bin/env python

#
# getSeqBlat.py
#
# author: Joseph Tran <Joseph.Tran@versailles.inra.fr>
# date: 25-03-2015
#

import argparse

## parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("modblat", help="modified blat alignment file in psl-like format: cf. QT")
args = parser.parse_args()
print args.modblat


