from Bio.Alphabet import generic_dna
from Bio.Seq import Seq
from numpy import loadtxt

__author__ = 'akarapetyan'


def Transcribing_DNA_into_RNA():
    temp = loadtxt('rosalind_rna.txt', dtype='str')
    temp = temp.tostring()
    DNA = Seq(temp, generic_dna)
    RNA = DNA.transcribe()
    print RNA

Transcribing_DNA_into_RNA()