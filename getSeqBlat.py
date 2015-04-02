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
parser.add_argument("modblat", help="modified blat alignment file in psl-like format (one header line, cf. QT)")

parser.add_argument("-U", "--target_upstream_fragment_size", dest="upstream_frag_sz", type=int, default=800, help="the target upstream fragment size to extract [default: %(default)s]")
parser.add_argument("-D", "--target_downstream_fragment_size", dest="downstream_frag_sz", type=int, default=4000, help="the target downstream fragment size to extract [default: %(default)s]")

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
        ### seq_id: Qname ; Tname ; LTR size; transcript size ; total size; RC if strand "-"
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
        logger.info("Loading modblat ...")
        if stat(args.modblat).st_size == 0:
            logger.error("modblat file is empty: " + args.modblat )
            sys.exit(1)
        else:
            logger.info("mod blat file: " + args.modblat)
            mb = ModBlat(args.modblat)

        logger.info("number of blat hits: " + str(len(mb.hits)))
        for hit in mb.hits:
            logger.log(0, "qname/tname pair: " + str(hit.qname) + "/" + str(hit.tname))

        ## compute genomic coordinates
        logger.info("Compute genomic bed items coordinates ...")
        bedItems= []
        for hit in mb.hits:
            bi = hit.computeGenomicSequenceBedItem(args.upstream_frag_sz, args.downstream_frag_sz)
            bedItems.append(bi.totuple())
        logger.info("number of bed items: " + str(len(bedItems)))

        ## export bed items to bed file
        logger.info("Export to bed file ...")
        bed = pybedtools.BedTool(bedItems)
        outfile = path.basename(path.splitext(args.modblat)[0]) + '_seqFlankBlatHit.bed'
        bed.saveas(outfile, trackline="track name='genomic sequence extraction flanking blat hit' color=128,0,0")
        num_lines = sum(1 for line in open(outfile))
        logger.info("number of lines in bed file: " + str(num_lines))

        ## get fasta sequence from bed
        logger.info("Get fasta sequences from bed ...")
        fasta_out = path.basename(path.splitext(args.modblat)[0]) + '_seqFlankBlatHit.fasta'
        bed = bed.sequence(fi=args.genome, s=True, name=True)
        bedout = bed.save_seqs(fasta_out)
        assert open(bedout.seqfn).read() == open(bed.seqfn).read()
        fout = Fasta(fasta_out)
        logger.info("flanking blat hits sequences file: " + fasta_out)
        logger.info("number of flanking sequences: " + str(len(sorted(fout.keys()))))
        if path.exists(fasta_out):
            unlink(fasta_out)

    except KeyboardInterrupt:
        print "Shutdown requested...exiting"
    except Exception:
        traceback.print_exc(file=sys.stdout)

### MAIN ###
if __name__ == '__main__':
    import sys, traceback
    from os import path, stat
    from pyfasta import Fasta
    from datetime import datetime
    import pybedtools
    #sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from getSeqBlatLib import ModBlatHit, ModBlat, BedItem

    startTime = datetime.now()

    main()

    logger.info("Execution time: " + str(datetime.now() - startTime))
    sys.exit(0)

