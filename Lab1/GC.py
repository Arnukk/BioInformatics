from Bio import SeqIO
from Bio.Alphabet import generic_dna
from Bio.Seq import Seq
from Bio.SeqUtils import *
from numpy import loadtxt

__author__ = 'akarapetyan'


def Computing_GC_Content():
    handle = open("rosalind_gc.txt", "rU")
    id = []
    seqgc = []
    for record in SeqIO.parse(handle, "fasta"):
        id.append(record.id)
        seqgc.append(GC(record.seq))
    handle.close()
    print id[seqgc.index(max(seqgc))], max(seqgc)

Computing_GC_Content()