from Bio.Alphabet import generic_dna
from Bio.Seq import Seq
from numpy import loadtxt

__author__ = 'akarapetyan'


def Complementing_Strand_of_DNA():
    temp = loadtxt('rosalind_revc.txt', dtype='str')
    temp = temp.tostring()
    DNA = Seq(temp, generic_dna)
    C_DNA = DNA.reverse_complement()
    print C_DNA

Complementing_Strand_of_DNA()