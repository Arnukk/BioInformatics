import numpy

__author__ = 'akarapetyan'
from numpy import zeros
Firstrow = []
Secondrow = []


def Backtracking(b, v, i, j, w):
    if i < 0 or j < 0:
        return
    if b[i, j] == "\\":
        Firstrow.append(list(v)[i-1])
        Secondrow.append(list(v)[i-1])
        Backtracking(b, v, i-1, j-1, w)
    else:
        if b[i, j] == "|":
            Firstrow.append(list(v)[i-1])
            Secondrow.append("-")
            Backtracking(b, v, i-1, j, w)
        elif b[i, j] == "<":
            Firstrow.append("-")
            Secondrow.append(list(w)[j-1])
            Backtracking(b, v, i, j-1, w)
        else:
            Firstrow.append(list(v)[i-1])
            Secondrow.append("-")
            Backtracking(b, v, i, j-1, w)


def lcs(v, w):
    n = len(v)
    m = len(w)
    s = zeros((n+1, m+1), dtype=int)
    b = zeros((n+1, m+1), dtype=str)

    for i in range(1, n+1):
        for j in range(1, m+1):
            if v[i-1] == w[j-1]:
                s[i, j] = s[i-1, j-1] + 1
            else:
                s[i, j] = max(s[i-1, j], s[i, j-1])
            if s[i, j] == s[i-1, j]:
                b[i, j] = "|"
            elif s[i, j] == s[i, j-1]:
                b[i, j] = "<"
            elif s[i, j] == s[i-1, j-1] + 1:
                b[i, j] = "\\"
    print s
    print s[n, m]
    print b
    Backtracking(b, v, n, m, w)
    Tworowmatrix = "".join(Secondrow) + "".join(Firstrow)
    Tworowmatrix = list(Tworowmatrix)
    Tworowmatrix = numpy.array(Tworowmatrix[::-1]).reshape(2, len(Firstrow))
    print "Here is the complete two row matrix with gaps\n"
    print Tworowmatrix


lcs ("ATCTGAT", "TGCATA")




