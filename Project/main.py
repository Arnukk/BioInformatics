__author__ = 'akarapetyan'
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import squareform
import os
import matplotlib.pyplot as plt
from numpy import loadtxt


def FindtheDistance(Genome1, Genome2):
    counter = 0
    for i in Genome1:
        if i in Genome2:
            counter += 1
    return (1.0/counter) * 1000


def heatmap(D, genomeNames, TheGenomeName):
    temp = D
    D = squareform(D)
    Y = linkage(D, method='average')
    fig = plt.figure(figsize=(18, 18))
    dendogram = fig.add_axes([0.01, 0.1, 0.1, 0.1])
    Z = dendrogram(Y, orientation='right')
    idx = Z['leaves']
    nothing = []
    for i in idx:
        nothing.append(TheGenomeName[genomeNames[i]])
    dendogram.set_yticklabels(nothing)
    D = D[idx, :][:, idx]
    matrix = fig.add_axes([0.25, 0.1, 0.7, 0.7])
    matrix.matshow(D, aspect='auto', origin='lower', cmap=plt.cm.YlGnBu)
    matrix.set_xticklabels(nothing)
    matrix.set_yticklabels([])
    plt.show()


def main():
    #Genome  names
    TheGenomeName = {}
    TheGenomeName['84588'] = 'Synechococcus sp. WH 8102'
    TheGenomeName['167539'] = 'Prochlorococcus marinus str. SS120'
    TheGenomeName['59919'] = 'Prochlorococcus marinus sp. MED4'
    TheGenomeName['74547'] = 'Prochlorococcus marinus str. MIT 9313'
    TheGenomeName['269084'] = 'Synechococcus elongatus PCC 6301'
    TheGenomeName['146891'] = 'Prochlorococcus marinus str. AS9601'
    TheGenomeName['74546'] = 'Prochlorococcus marinus str. MIT 9312'
    TheGenomeName['321327'] = 'Synechococcus sp. JA-3-3Ab'
    TheGenomeName['321332'] = "Synechococcus sp. JA-2-3B'a(2-13)"
    TheGenomeName['64471'] = 'Synechococcus sp. CC9311'
    TheGenomeName['221359'] = 'Synechococcus sp. RS9916'
    TheGenomeName['313625'] = 'Synechococcus sp. BL107'
    TheGenomeName['32049'] = 'Synechococcus sp. PCC 7002'
    TheGenomeName['59931'] = 'Synechococcus sp. WH 7805'
    TheGenomeName['69042'] = 'Synechococcus sp. WH 5701'
    TheGenomeName['316278'] = 'Synechococcus sp. RCC307'
    TheGenomeName['32051'] = 'Synechococcus sp. WH 7803'
    TheGenomeName['59920'] = 'Prochlorococcus marinus str. NATL2A'
    TheGenomeName['59922'] = 'Prochlorococcus marinus str. MIT 9303'
    TheGenomeName['167542'] = 'Prochlorococcus marinus str. MIT 9515'
    TheGenomeName['167546'] = 'Prochlorococcus marinus str. MIT 9301'
    TheGenomeName['167555'] = 'Prochlorococcus marinus str. NATL1A'
    TheGenomeName['93059'] = 'Prochlorococcus marinus str. MIT 9211'
    TheGenomeName['93060'] = 'Prochlorococcus marinus sp. MIT9215'

    CurrDir = os.getcwd()
    Genomes = {}
    #reading the genes from the input files
    for files in os.walk(CurrDir):
        for file in files:
            pass
    for i in file:
        if i.endswith('.csv'):
            Genomes[i[0:-4]] = loadtxt(i, dtype='str')
            Genomes[i[0:-4]] = Genomes[i[0:-4]].tolist()
            Genomes[i[0:-4]].remove(Genomes[i[0:-4]][0])
    #Finding genes that are common in all the genomes [just brute force]
    Matches = []
    for i in Genomes.values():
        for j in i:
            flag = False
            for x in Genomes.values():
                if x != i:
                    if j in x:
                        flag = True
                    else:
                        flag = False
                        break
            if flag:
                if j not in Matches:
                    Matches.append(j)
    #Now lets create the 'distance' matrix based on the number of genes that the genomes have in common
    GenomeTemp = []
    GenomeNames = []
    for key, val in Genomes.items():
        GenomeTemp.append(val)
        GenomeNames.append(key)
    distances = []
    for i in range(0, len(GenomeTemp)-1, 1):
        for j in range(i+1, len(GenomeTemp), 1):
            distances.append(FindtheDistance(GenomeTemp[i], GenomeTemp[j]))
    print distances
    heatmap(distances, GenomeNames, TheGenomeName)

main()