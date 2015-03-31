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

def main():
    try:
        ### steps ###
        ## load genome
        ## load mod blat
        ## iterate over blat hits and extract genomic sequences regarding the given fragment sizes (transcript and LTR) at the reference position
        ### 2 cases: strand + or -
        ## export bed with sequence coordinates to extract
        ## export fasta output using pybedtools
        ### seq_id: Qname ; Tname ; LTR size; transcript size ; total size
        ### seq

        ## load genome
        logger.info("Loading fasta genome ...")
        if stat(args.genome).st_size == 0:
            logger.error("genome file is empty: " + args.genome )
            sys.exit(1)
        else:
            fasta = Fasta(args.genome)
            logger.info("genome file: " + args.genome)
            logger.info("number of reference sequences: " + str(len(sorted(fasta.keys()))))
        

        ## load mod blat
        logger.info("mod blat file: " + args.modblat)
        modblathits = []
        fp = open(args.modblat)
        with fp as f:
            # skip header line
            next(f)
            for line in f:
                hit = ModBlatHit(line)
                modblathits.append(hit)

        logger.info("number of blat hits: " + str(len(modblathits)))
        for hit in modblathits:
            logger.log(0, "qname/tname pair: " + str(hit.qname) + "/" + str(hit.tname))
    
    except KeyboardInterrupt:
        print "Shutdown requested...exiting"
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

### MAIN ###
if __name__ == '__main__':
    import sys, traceback
    from os import path, stat
    from pyfasta import Fasta
    #sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from getSeqBlatLib import ModBlatHit

    main()
