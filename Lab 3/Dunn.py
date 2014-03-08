__author__ = 'akarapetyan'

from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt


def clusterDistances(cluster1, cluster2, DM):
    return DM[cluster1][:, cluster2].mean()


def Dunn(clustering, DM):
    pass


def heatmap(D):
    Y = linkage(squareform(D), method='average')
    fig = plt.figure(figsize=(8, 8))
    dendogram = fig.add_axes([0.01, 0.1, 0.1, 0.8])
    Z = dendrogram(Y, orientation='right')
    idx = Z['leaves']
    dendogram.set_yticklabels(idx)
    D = D[idx, :][:, idx]
    matrix = fig.add_axes([0.37, 0.1, 0.6, 0.8])
    im = matrix.matshow(D, aspect='auto', origin='lower', cmap=plt.cm.YlGnBu)
    matrix.set_xticklabels([])
    matrix.set_yticklabels([])
    plt.show()

D = squareform([1, 5, 6, 0.9, 4, 5, 0.1, 1, 4.1, 5.1])
heatmap(D)
print Dunn([[0, 1, 4], [2, 3]], D)


