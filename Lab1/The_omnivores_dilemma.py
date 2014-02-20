from Bio import SeqIO
from Bio.Alphabet import generic_dna
from Bio.Seq import Seq
import numpy as np
import matplotlib.pyplot as plt


__author__ = 'akarapetyan'

def The_omnivores_dilemma():
    cucumber_handle = open("cucumber.fasta", "rU")
    cucumber_dna = []
    for record in SeqIO.parse(cucumber_handle, "fasta"):
        cucumber_dna.append(Seq(record.seq.tostring()[21:570], generic_dna))
    eagle_handle = open("eagle.fasta", "rU")
    eagle_dna = []
    for record in SeqIO.parse(eagle_handle, "fasta"):
        eagle_dna.append(Seq(record.seq.tostring()[399:1521], generic_dna))
    Amino_acids = {}
    Amino_acids["Ala"] = [["GCT", "GCC", "GCA", "GCG"], 0]
    Amino_acids["Arg"] = [["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"], 0]
    Amino_acids["Asn"] = [["AAT", "AAC"], 0]
    Amino_acids["Asp"] = [["GAT", "GAC"], 0]
    Amino_acids["Cys"] = [["TGT", "TGC"], 0]
    Amino_acids["Gln"] = [["CAA", "CAG"], 0]
    Amino_acids["Glu"] = [["GAA", "GAG"], 0]
    Amino_acids["Gly"] = [["GGT", "GGC", "GGA", "GGG"], 0]
    Amino_acids["His"] = [["CAT", "CAC"], 0]
    Amino_acids["Ile"] = [["ATT", "ATC", "ATA"], 0]
    Amino_acids["Leu"] = [["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"], 0]
    Amino_acids["Lys"] = [["AAA", "AAG"], 0]
    Amino_acids["Met"] = [["ATG"], 0]
    Amino_acids["Phe"] = [["TTT", "TTC"], 0]
    Amino_acids["Pro"] = [["CCT", "CCC", "CCA", "CCG"], 0]
    Amino_acids["Ser"] = [["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"], 0]
    Amino_acids["Thr"] = [["ACT", "ACC", "ACA", "ACG"], 0]
    Amino_acids["Trp"] = [["TGG"], 0]
    Amino_acids["Tyr"] = [["TAT", "TAC"], 0]
    Amino_acids["Val"] = [["GTT", "GTC", "GTA", "GTG"], 0]
    Amino_acids["Ile"] = [["ATT", "ATC", "ATA"], 0]

    cucumber_statistics = []
    eagle_statistics = []
    xlabels = []
    for key in Amino_acids.keys():
        count_cucumber = 0
        count_eagle = 0
        xlabels.append(key)
        for item in Amino_acids[key][0]:
            count_cucumber += cucumber_dna[0].count(item)
            count_eagle += eagle_dna[0].count(item)
        cucumber_statistics.append(count_cucumber)
        eagle_statistics.append(count_eagle)
    print eagle_statistics
    print cucumber_statistics

    N = len(xlabels)
    Eagle_vals = (eagle_statistics)
    Cucumber_vals = (cucumber_statistics)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.5       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, Eagle_vals,   width, color='r')
    p2 = plt.bar(ind, Cucumber_vals, width, color='y')

    plt.ylabel('Quantity')
    plt.title('Quantity of amino acids in Eagle\'s and Cucumber\'s DNA sequences')
    plt.xticks(ind+width/2., xlabels)
    plt.yticks(np.arange(0, 150, 5))
    plt.legend((p1[0], p2[0]), ('Eagle', 'Cucumber'))

    plt.show()



The_omnivores_dilemma()