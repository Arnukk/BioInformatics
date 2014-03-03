
__author__ = 'akarapetyan'

from numpy import zeros
gap = -1
seq1 = 'PRETERIT'
seq2 = 'VEITGEIST'


def glb_lcs(v, w):
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
                s[i-1, j-1] + delta(v[i-1], w[j-1]),
                0
            )
    print s


def delta(a, b):
    if a == b:
        return 1
    else:
        return 0

glb_lcs(seq1, seq2)
