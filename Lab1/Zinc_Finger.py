__author__ = 'akarapetyan'

from Bio import SeqIO
from Bio.Alphabet import generic_rna
from Bio.Seq import Seq
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.pyplot import matshow, xticks, yticks, show, gca
import numpy as np




def Zinc_Finger():
    handle = open("NM_002383.fasta", "rU")
    rna = []
    for record in SeqIO.parse(handle, "fasta"):
        rna.append(Seq(record.seq.tostring()[165:1599], generic_rna))
    v = rna[0].tostring()
    w = rna[0].tostring()

    m = len(v)
    n = len(w)

    dotmatrix = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            if v[i] == w[j]:
                dotmatrix[i][j] = 1


    matshow(dotmatrix)
    xticks(np.arange(len(w)), list(w))
    yticks(np.arange(len(v)), list(v))
    show()
    handle.close()

Zinc_Finger()
