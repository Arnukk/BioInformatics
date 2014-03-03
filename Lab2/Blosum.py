__author__ = 'akarapetyan'


from numpy import zeros
from Bio.SubsMat import MatrixInfo
from pylab import *



seq1 = 'PRETERIT'
seq2 = 'VEITGEIST'
gap = -1
blosum = MatrixInfo.blosum62


def score_match(pair):
    if pair not in blosum:
        return blosum[(tuple(reversed(pair)))]
    else:
        return blosum[pair]

def BLOSUM(v, w, gap, score_match):
    n = len(v)
    m = len(w)
    s = zeros((n+1, m+1), dtype=int)
    s[0][:] = range(0, -n-2, -1)
    s[:, 0] = range(0, -m, -1)
    for i in range(1, n+1):
        for j in range(1, m+1):
            s[i, j] = max(
                s[i-1, j] + gap,
                s[i, j-1] + gap,
                s[i-1, j-1] + score_match((v[i-1], w[j-1]))
            )
    fig = plt.figure()
    ax = plt.gca()
    nrows, ncols = n+1, m
    hcell, wcell = 0.5, 1.
    hpad, wpad = 0, 0

    fig=plt.figure(figsize=(ncols*wcell+wpad, nrows*hcell+hpad))
    ax = fig.add_subplot(111)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    colLabels = list(seq2)
    colLabels.insert(0, ' ')
    rowLabels = list(seq1)
    rowLabels.insert(0, ' ')
    table = ax.table(cellText=s, rowLabels=rowLabels, colLabels=colLabels,  loc='center')
    table.set_zorder(10)
    plt.text(100, 80, table)
    plt.show()
    print s

BLOSUM(seq1, seq2, gap, score_match)