from Bio import SeqIO
from Bio.Alphabet import generic_rna
from Bio.Seq import Seq


__author__ = 'akarapetyan'


def mrna_to_protein():
    handle = open("actn3.fasta", "rU")
    messenger_rna = []
    for record in SeqIO.parse(handle, "fasta"):
        messenger_rna.append(Seq(record.seq.tostring()[97:2803], generic_rna))
    protein = messenger_rna[0].translate()
    print protein
    handle.close()

mrna_to_protein()