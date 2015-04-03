# getSeqFlankBlatHit
Getting sequences flanking blat hits

Extraction des séquences flanquant les hits blat.

## Contexte
  
L'extraction de séquences flanquantes se fait en amont et en aval d'un hit blat:
- en amont du hit blat: p.ex 800pb
- en aval du hit blat: p.ex 4000pb

Attention à l'orientation du brin: +/-
- hit brin '+'
target 5' __________________ 3'
            |||||||||
            ------>
  800pb <=  *Tstart  => 4000pb

- hit brin '-'
target 5' __________________ 3'
            |||||||||
               <-----
     4000pb <=  Tend*  => 800pb

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

- fichier fasta contenant la référence (ex: génome)
- fichier blat modifié (ne contient plus qu'une seule ligne d'en-tête)

### output

- fichier bed contenant les coordonnées des séquences flanquantes
- fichier fasta contenant les séquences flanquantes


## Dépendances
  
### lib
 
- getSeqFlankBlatHitLib

### modules python
  
- cython
- numpy
- pybedtools
- pyfasta
- virtualenv (optionnel)
- nose (optionnel)

### tools
  
- bedtools (>=2.23.0)


## Installation détaillée

#### install utils

```
sudo easy_install pip

```

#### bedtools

```
# macosx
brew install homebrew/science/bedtools
# or
port install bedtools

# linux/debian/ubuntu
apt-get install bedtools

# linux fedora/redhat/centos
yum install BEDTools

```

#### virtualenv

```
sudo pip install virtualenv

# optional: 
# create a virtual env
virtualenv getSeqFlankBlatHit
# activate
source getSeqFlankBlatHit/bin/activate
# deactivate
deactivate

```
#### numpy

```
# for all users
sudo pip install numpy
# or use virtualenv
pip install numpy

```

#### pyfasta

```
# for all users
sudo pip install pyfasta
# or use virtualenv
pip install pyfasta

```

#### cython

```
# for all users
sudo pip install -U cython
# or use virtualenv
pip install -U cython

```

#### pybedtools

```
# on macosx
# workaround to fix clang error
# the ARCHFLAGS is needed to skip error at install
# [fix clang error](https://kaspermunck.github.io/2014/03/fixing-clang-error/)
sudo ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install pybedtools

# or use virtualenv
ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install pybedtools

```

#### clone getSeqFlankBlatHit

```
git clone https://github.com/jos4uke/getSeqFlankBlatHit.git


## make script executable
chmod 755 getSeqFlankBlatHit/getSeqFlankBlatHit.py

```

#### configure PATH

```
## edit .profile or .bashrc, etc.
'''
## getSeqFlankBlatHit
export PATH=/Users/qtbui/Documents/QUYNH_TRANG/Travail_QT/Scripts_QT/getSeqFlankBlatHit:$PATH
'''
source ~/.profile

```


# Exemple

### Input

#### genome

```
grep '>' data/genome_exemple.fa
>gb|AWOK01290555.1| Nicotiana tabacum, whole genome shotgun sequence
>gb|AWOK01220183.1| Nicotiana tabacum, whole genome shotgun sequence

```

#### modblat

```
cat data/modblat_exemple.psl
match	mis.match	rep_match	countN	Qgapcount	Qgapbases	Tgapcount	Tgapbases	strand	Qname-Tnt1	Qsize	Qstart	Qend	Tname	Tsize	Tstart	Tend	blockcount	blockSizes	qStarts	tStarts
299     0       0       0       0       0       2       371     +       mira_rep_c6170  299     0       299     gb|AWOK01290555.1|      13594   284     954     3       6,69,224,	0,6,75, 284,660,730,
223     0       0       0       0       0       0       0       -       mira_rep_c6837  228     0       223     gb|AWOK01220183.1|      13081   7548    7771    1       223     5	7548

```

### Run

```
python getSeqFlankBlatHit.py -U 615 -D 4000 data/genome_exemple.fa data/modblat_exemple.psl 
2015-04-03 15:01:34,086 - getSeqFlankBlatHit - INFO - Loading fasta genome ...
2015-04-03 15:01:34,128 - getSeqFlankBlatHit - INFO - genome file: genome_exemple.fa
2015-04-03 15:01:34,129 - getSeqFlankBlatHit - INFO - number of reference sequences: 2
2015-04-03 15:01:34,129 - getSeqFlankBlatHit - INFO - Loading modblat ...
2015-04-03 15:01:34,129 - getSeqFlankBlatHit - INFO - mod blat file: modblat_exemple.psl
2015-04-03 15:01:34,129 - getSeqFlankBlatHit - INFO - number of blat hits: 2
2015-04-03 15:01:34,129 - getSeqFlankBlatHit - INFO - Compute genomic bed items coordinates ...
2015-04-03 15:01:34,129 - getSeqFlankBlatHit - INFO - number of bed items: 2
2015-04-03 15:01:34,129 - getSeqFlankBlatHit - INFO - Export to bed file ...
2015-04-03 15:01:34,132 - getSeqFlankBlatHit - INFO - number of lines in bed file: 3
2015-04-03 15:01:34,133 - getSeqFlankBlatHit - INFO - Get fasta sequences from bed ...
index file genome_exemple.fa.fai not found, generating...
2015-04-03 15:01:34,318 - getSeqFlankBlatHit - INFO - flanking blat hits sequences file: data/modblat_exemple_seqFlankBlatHit.fasta
2015-04-03 15:01:34,318 - getSeqFlankBlatHit - INFO - number of flanking sequences: 2
2015-04-03 15:01:34,319 - getSeqFlankBlatHit - INFO - Execution time: 0:00:00.232825


```

### Output

#### bed

```
cat data/modblat_exemple_getSeqFlankBlatHit.bed
track name='genomic sequence extraction flanking blat hit' color=128,0,0
gb|AWOK01158785.1|      0       3206    mira_rep_c6836 ; gb|AWOK01158785.1| ; 0:3206 ; 3207 ; rc        0       reverse
gb|AWOK01318317.1|      5211    9826    mira_c148 ; gb|AWOK01318317.1| ; 5211:9826 ; 4616       0       forward

```

#### fasta

```
grep '>' data/modblat_exemple_getSeqFlankBlatHit.fasta
>mira_rep_c6170 ; gb|AWOK01290555.1| ; 0:4284 ; 4285
>mira_rep_c6837 ; gb|AWOK01220183.1| ; 3771:8386 ; 4616 ; rc

```


