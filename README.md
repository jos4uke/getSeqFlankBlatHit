# getSeqFlankBlatHit
Getting sequences flanking blat hits

Extraction des s�quences flanquant les hits blat.

## D�pendances
  
### lib
 
- getSeqFlankBlatHitLib

### modules python
  
- pybedtools
- pyfasta
- cython
- virtualenv (optionnel)
- nose (optionnel)

### tools
  
- bedtools (>=2.23.0)

## Contexte
  
L'extraction de s�quences flanquantes se fait en amont et en aval d'un hit blat:
- en amont de la LTR: p.ex 800pb
- en aval de la LTR: p.ex 4000pb

Attention � l'orientation du brin: +/-
- hit brin '+'
       __________________
           |||||||||
           ------>
  800pb <= *Tstart  => 4000pb

- hit brin '-'
       __________________
           |||||||||
              <-----
     4000pb <= Tend*  => 800pb

## Help

```
python getSeqFlankBlatHit.py --help
usage: getSeqFlankBlatHit.py [-h] [-U UPSTREAM_FRAG_SZ]
                             [-D DOWNSTREAM_FRAG_SZ]
                             genome modblat

Extract genomic sequences flanking blat hits

positional arguments:
  genome                genome in fasta format
  modblat               modified blat alignment file in psl-like format (one
                        header line, cf. QT)

optional arguments:
  -h, --help            show this help message and exit
  -U UPSTREAM_FRAG_SZ, --target_upstream_fragment_size UPSTREAM_FRAG_SZ
                        the target upstream fragment size to extract [default:
                        800]
  -D DOWNSTREAM_FRAG_SZ, --target_downstream_fragment_size DOWNSTREAM_FRAG_SZ
                        the target downstream fragment size to extract
                        [default: 4000]


```

### input

- fichier fasta contenant la r�f�rence (ex: g�nome)
- fichier blat modifi� (ne contient plus qu'une seule ligne d'en-t�te)

### output

- fichier bed contenant les coordonn�es des s�quences flanquantes
- fichier fasta contenant les s�quences flanquantes




