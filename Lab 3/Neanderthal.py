__author__ = 'akarapetyan'
from Bio import SeqIO
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt
import numpy as np


def levenshtein(a, b):
    edt = 0
    for i in range(0, len(a), 1 ):
        if a[i] != b[i]:
            edt += 1
    return edt



def clusterDistances(cluster1, cluster2, DM):
    return DM[cluster1][:, cluster2].mean()


def Dunn(clustering, DM):
    clusters = len(clustering)
    maxIntra = max([clusterDistances(c, c, DM) for c in clustering])
    minInter = np.inf
    for cl1 in range(1, clusters):
        for cl2 in range(cl1):
            minInter = min(clusterDistances(clustering[cl1], clustering[cl2], DM), minInter)
    if maxIntra != 0:
        return minInter/maxIntra
    else:
        return np.inf


def flatclusterDunn(D):
    DM = squareform(D)
    Y = linkage(DM, method="average")
    n = len(Y)+1
    clusterdict = dict([(el, [el]) for el in range(n)])
    bestClustering, bestDunn = None, 0
    for cidx, cluster in enumerate(Y):
        cl1, cl2 = map(int, cluster[:2])
        clusterdict[cidx+n] = clusterdict[cl1] + clusterdict[cl2]
        del clusterdict[cl1]
        del clusterdict[cl2]
        clustering = clusterdict.values()
        if not len(clustering) in [1, n]:
            currentDunn = Dunn(clustering, DM)
            print (clustering, currentDunn)
            if currentDunn > bestDunn:
                bestDunn = currentDunn
                bestClustering = clustering
    print "The Best clustering with a maximal Dunn index is", bestClustering, bestDunn


def heatmap(D):
    temp = D
    D = squareform(D)
    Y = linkage(D, method='average')
    fig = plt.figure(figsize=(18, 18))
    dendogram = fig.add_axes([0.01, 0.1, 0.75, 0.8])
    Z = dendrogram(Y, orientation='right')
    idx = Z['leaves']
    dendogram.set_yticklabels(idx)
    D = D[idx, :][:, idx]
    matrix = fig.add_axes([0.8, 0.1, 0.17, 0.3])
    im = matrix.matshow(D, aspect='auto', origin='lower', cmap=plt.cm.YlGnBu)
    matrix.set_xticklabels([])
    matrix.set_yticklabels([])
    plt.show()
    flatclusterDunn(temp)


def main():
    mitoHandle = open("mitoAligned.fa", "rU")
    mitoSeqs = []
    for record in SeqIO.parse(mitoHandle, "fasta"):
        mitoSeqs.append(record.seq.tostring())
    distances = []
    for i in range(0, len(mitoSeqs)-1, 1):
        for j in range(i+1, len(mitoSeqs), 1):
            distances.append(float(levenshtein(mitoSeqs[i], mitoSeqs[j])))
    heatmap(distances)

main()

