from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle

__author__ = 'akarapetyan'
from matplotlib.pyplot import matshow, xticks, yticks, show, gca
import numpy as np


def dotplot():
    v = "JKSDGFUDSFSDLKFHUISDNFSLDLNFBUISDGBSDFLBDSHIOFVBDLJSBDKJSFBGHDSFGBHDSFGS"
    w = "SDDSRHWE*UHSDKFBDIHBSDMBIUGSDLKSNHJDSGVBFSDODSNBIDSHGBFSDDSFSDJKLGFSDLJK"
    newwin = 26
    threshhold = 5

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
    gca().add_patch(Rectangle((len(w)/2-newwin/2, len(v)/2-newwin/2), newwin, newwin, color='white', alpha=0.5))
    d = np.arange(len(w))
    c = np.arange(len(v))
    gca().plot(c, d)
    show()



    y = np.arange(len(v)/2-newwin/2, len(v)/2+newwin/2)
    x = np.arange(len(w)/2-newwin/2, len(w)/2+newwin/2)
    newmat =  np.asmatrix(dotmatrix[np.ix_(y,x)])

    if (np.sum(newmat.diagonal()) < threshhold):
        for i in range((len(v)/2)-(newwin/2),(len(v)/2)+(newwin/2)):
            for j in range((len(w)/2)-(newwin/2),(len(w)/2)+(newwin/2)):
                    dotmatrix[i][j] = 0


    matshow(dotmatrix)
    xticks(np.arange(len(w)), list(w))
    yticks(np.arange(len(v)), list(v))
    gca().add_patch(Rectangle((len(w)/2-newwin/2, len(v)/2-newwin/2), newwin, newwin, color='white', alpha=0.5))
    d = np.arange(len(w))
    c = np.arange(len(v))
    gca().plot(c, d)
    show()


dotplot()



