from Bio.Alphabet import generic_dna

__author__ = 'akarapetyan'
from numpy import *
from Bio import Seq


def DNANucleotides():
    DNA = loadtxt('rosalind_dna.txt', dtype='str')
    DNA = DNA.tostring()
    My_DNA = Seq.Seq(DNA, generic_dna)
    A = My_DNA.count('A')
    C = My_DNA.count('C')
    G = My_DNA.count('G')
    T = My_DNA.count('T')
    print A, C, G, T

DNANucleotides()
