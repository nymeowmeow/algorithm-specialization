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

if __name__ == '__main__':
    edges = []
    nodeset = set()
    with open('clustering1.txt', 'r') as f:
         nodecount = int(f.readline().strip())
         for line in f:
             item = line.strip().split()
             assert(len(item) == 3)
             fromnode = int(item[0])
             tonode = int(item[1])
             weight = int(item[2])
             nodeset.add(fromnode)
             nodeset.add(tonode)
             edges.append((fromnode, tonode, weight))

    print ('node count: {}, number of edges: {}, count: {}'.format(nodecount, len(edges), len(nodeset)))
    edges = sorted(edges, key = lambda edge: edge[-1])
    nodemap = { n : UnionNode(n) for n in nodeset }

    while len(nodeset) >= 4:
        (fromnode, tonode, weight) = edges.pop(0)

        parent, other = union(nodemap[fromnode], nodemap[tonode])
        if other is not None and other in nodeset:
            nodeset.remove(other)

    print ('weight : {}, number of clusters: {}'.format(weight, len(nodeset)))
             
             