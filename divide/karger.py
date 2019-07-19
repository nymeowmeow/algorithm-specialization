import sys
import math
import random

class UnionNode(object):
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.rank = 0

def find(node):
    mynode = node
    while mynode.parent is not None:
        mynode = mynode.parent
    return mynode

def union(node1, node2):
    parent1 = find(node1)
    parent2 = find(node2)

    if parent1 is not parent2:
        if parent1.rank < parent2.rank:
            parent1.parent = parent2
        elif parent1.rank > parent2.rank:
            parent2.parent = parent1
        else:
            parent2.parent = parent1
            parent1.rank += 1
        
def calculateMinCut(nodes, edges):
    random.shuffle(edges) #randomized the edges at once
    nodemap = { n:UnionNode(n) for n in nodes }

    i = 0
    nodecount = len(nodes)
    while nodecount > 2:
        n1, n2 = edges[i]
        p1 = find(nodemap[n1])
        p2 = find(nodemap[n2])

        if p1 is not p2:
            union(p1, p2)
            nodecount -= 1
        i += 1

    #the partition is done, remove edges that are within the same cluster
    edgelist = []
    for e in edges:
        n1, n2 = e
        p1 = find(nodemap[n1])
        p2 = find(nodemap[n2])
        if p1 is not p2:
            edgelist.append(e)
    return len(edgelist), edgelist

if __name__ == '__main__':
    with open('kargermincut.txt', 'r') as f:
        lines = f.readlines()
        nodes = []
        edges = []
        for line in lines:
            n = line.split()
            nodes.append(n[0])
            edges.extend([ (n[0], nn) for nn in n[1:] ])

    nodecount = len(nodes)
    trails = nodecount**2 * math.ceil(math.log(nodecount))
    trails = 20000
    print ('trails: {}'.format(trails))
    mincut = nodecount #initialize to max value
    for i in range(trails):
        cut, edgelist = calculateMinCut(nodes, edges)
        if i % 1000 == 0:
            print ('cut is {}, min cut is {}, count {}'.format(cut, mincut, i))
        if cut < mincut:
            mincut = cut

    print ("min cut is {}".format(mincut/2))
