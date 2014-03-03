__author__ = 'akarapetyan'
import scipy.spatial.distance as dist
import scipy.cluster.hierarchy as sch


def main():
    myarray = [[0,1,5,6,0.9]
                    [1,0,4,5,0.1]
                    [5,4,0,1,4.1]
                    [6,5,1,0,5.1]
                    [0.9,0.1,4.1,5.1,0]]
    print sch.linkage(dist.squareform(myarray), method='average')


main()