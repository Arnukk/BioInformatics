from Bio import SeqIO
from Bio.Alphabet import generic_dna
from Bio.Seq import Seq
from Bio.SeqUtils import *
from numpy import loadtxt

__author__ = 'akarapetyan'


def Counting_Point_Mutation():
    temp = loadtxt('rosalind_hamm.txt', dtype='str')
    k = 0
    DNA1 = temp[0].tostring()
    DNA2 = temp[1].tostring()
    for i in range(0, len(DNA1), 1):
        if DNA1[i] != DNA2[i]:
            k += 1

    print k

Counting_Point_Mutation()
