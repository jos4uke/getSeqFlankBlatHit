#!/usr/bin/env python

#
# getSeqBlat.py
#
# author: Joseph Tran <Joseph.Tran@versailles.inra.fr>
# date: 25-03-2015
#

# Extraire des séquences à partir du résultat blat (query=rétro,mira,...; database=génome du tabac):
# Fichiers inputs= génome au format fasta; output du blat modifié en txt (Ex: "BLAT_BX_contigs_Tnt1.txt")
# Nom de la seq à extraire=dans la colonne "Tname"; le nom de la séq extraite=dans la colonne "Qname". 
# Extraire la seq: 
# Si "strand +" => "Nbr bp à extraire" upstream à partir de la position Tstart et 4000pb downstream. 
# Si "strand -" => "Nbr pb à extraire" downstream à partir de la position Tend et 4000pb upstream en reverse complémentaire

import argparse

## parse arguments
parser = argparse.ArgumentParser(description="Extraire les séquences génomiques à partir d'un résultat blat")

parser.add_argument("modblat", help="modified blat alignment file in psl-like format: cf. QT")
parser.add_argument("genome", help="genome in fasta format")

parser.add_argument("-t", "--target_transcript_fragment_size", dest="tt_frag_sz", type=int, default=4000, help="the target transcript fragment size to extract [default: %(default)s]")

args = parser.parse_args()

print args.tt_frag_sz

