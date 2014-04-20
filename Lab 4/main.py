import random

__author__ = 'akarapetyan'
import networkx as nx
import matplotlib.pyplot as plt


def main():
    genome = 'ATGGCGTGCA'
    kmers = []
    k = 3
    for i in range(len(genome) - k + 1):
        kmers.append(genome[i:i+k])
    Graph = nx.DiGraph()
    for i in kmers:
        Graph.add_edge(i[0:2], i[1:3])

    nx.draw(Graph)
    plt.show()
    for i in Graph.nodes():
        if Graph.in_degree(i) != Graph.out_degree(i):
            print "Node %s is unbalanced" % i
        if Graph.in_degree(i) - Graph.out_degree(i) == 1:
            end = i
            print "Node %s is the End node" % i
        if Graph.in_degree(i) - Graph.out_degree(i) == -1:
            start = i
            print "Node %s is the Start node" % i
    print "Is this Graph Eulerian ? - %s" % nx.is_eulerian(Graph)
    Graph.add_edge(end, start)
    print "I have made some changes, is this Graph Eulerian now ? - %s" % nx.is_eulerian(Graph)

    MaxOutDegree = -1
    for i in Graph.nodes():
        MaxOutDegree = Graph.out_degree(i) if Graph.out_degree(i) > MaxOutDegree else -1
    paths = []

    while len(paths) < MaxOutDegree:
        temp = []
        TempGraph = Graph.copy()
        path = FindEulerianCycles(TempGraph, start, temp, end)
        if path not in paths and len(path) > 0:
            paths.append(path)
    print paths


def FindEulerianCycles(Graph, start, path, end):
    node = start
    if not Graph.successors(node):
        return path
    path.append(node)
    if isinstance(Graph.successors(node), list) and len(Graph.successors(node)) > 1:
        Randnode = random.randint(0, len(Graph.successors(node))-1)
        while Graph.successors(node)[Randnode] == end:
            Randnode = random.randint(0, len(Graph.successors(node))-1)
        start = Graph.successors(node)[Randnode]
        Graph.remove_edge(node, start)
        return FindEulerianCycles(Graph, start, path, end)
    else:
        start = Graph.successors(node)[0]
        Graph.remove_edge(node, start)
        return FindEulerianCycles(Graph, start, path, end)


main()





