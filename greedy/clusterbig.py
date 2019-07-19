import itertools

class UnionNode(object):
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0

def find(node):
    mynode = node
    while mynode.parent is not mynode:
        mynode = mynode.parent
    return mynode

def union(node1, node2):
    parent1 = find(node1)
    parent2 = find(node2)

    p = parent1
    other = None
    if parent1 is not parent2:
        if parent1.rank < parent2.rank:
            parent1.parent = parent2
            p = parent2
            other = parent1
        elif parent1.rank > parent2.rank:
            parent2.parent = parent1
            p = parent1
            other = parent2
        else:
            parent2.parent = parent1
            parent1.rank += 1
            p = parent1
            other = parent2

    return p.id, (other.id if other is not None else None)

def getNeighbors(node, k):
    neighbor = []
    indexes = itertools.combinations(range(len(node)), k)
    for index in indexes:
        s = list(node)
        for pos in index:
            s[pos] = '1' if s[pos] == '0' else '0'

        neighbor.append(''.join(s))
    return neighbor

if __name__ == '__main__':
    nodeset = set()
    with open('clustering_big.txt', 'r') as f:
         nodecount = int(f.readline().strip().split()[0])
         for line in f:
             item = ''.join(line.strip().split())
             nodeset.add(item)

    print ('node count: {}, count: {}'.format(nodecount, len(nodeset)))
    nodemap = { n : UnionNode(n) for n in nodeset }

    k = 2
    for i in range(1, k+1):
        for node in nodemap.keys():
            neighbor = getNeighbors(node, i)

            for n in neighbor:
                if n not in nodemap:
                    continue
                parent, other = union(nodemap[node], nodemap[n])
                if other is not None and other in nodeset:
                    nodeset.remove(other)

    print ('number of clusters: {}'.format(len(nodeset)))
             
             