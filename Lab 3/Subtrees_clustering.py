from sympy.utilities.tests.test_lambdify import numpy

__author__ = 'akarapetyan'
from scipy.cluster.hierarchy import linkage
import scipy.spatial.distance as dist



def flatclusters(Z, threshhold):
    Z = numpy.array(Z)
    i = 0
    response = []
    while i < len(Z):
        if Z[i][2] > threshhold:
            response = numpy.delete(Z, i, 0)
        i += 1
    return response




def main():
    myarray = [[0,1,5,6,0.9],
                [1,0,4,5,0.1],
                [5,4,0,1,4.1],
                [6,5,1,0,5.1],
                [0.9,0.1,4.1,5.1,0]]
    Z = linkage(dist.squareform(myarray), method='average')
    print flatclusters(Z, 1.1)


main()