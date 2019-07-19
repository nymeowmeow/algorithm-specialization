import heapq
from collections import defaultdict

class PriorityQueue(object):
    def __init__(self, heap = []):
       heapq.heapify(heap)
       self.heap = heap
       self.entry_finder = dict({i[-1] : i for i in heap})
       self.REMOVED = -123456

    def insert(self, node, priority = 0):
        if node in self.entry_finder:
            self.delete(node)

        entry = [priority, node]
        self.entry_finder[node] = entry
        heapq.heappush(self.heap, entry)

    def delete(self, node):
        entry = self.entry_finder.pop(node)
        entry[-1] = self.REMOVED
        return entry[0]

    def pop(self):
       while self.heap:
           priority, node = heapq.heappop(self.heap)
           if node is not self.REMOVED:
              del self.entry_finder[node]
              return priority, node
       raise KeyError('pop from an empty priority queue')

if __name__ == '__main__':
    edges = defaultdict(list)
    with open('edges.txt', 'r') as f:
        next(f)
        for line in f:
            item = line.strip().split()
            assert(len(item) == 3)
            first = int(item[0])
            second = int(item[1])
            weight = int(item[2])
            #undirected graph
            edges[first].append((second, weight))
            edges[second].append((first, weight))

    maxvalue = 10000
    print (len(edges))
    heap = []
    source = 1
    sourcedict = dict(edges[source])
    for node, value in edges.items():
         if node == 1:
             continue
         elif node in sourcedict:
             heap.append([sourcedict[node], node])
         else:
             heap.append([maxvalue, node])
    queue = PriorityQueue(heap)
    mst = []
    processed = [ source ]
    candidate = set([ node[1] for node in queue.heap ])
    while candidate:
        dist, node = queue.pop()
        processed.append(node)
        mst.append(dist)
        candidate.remove(node)
        for (nextnode, weight) in edges[node]:
            if nextnode in candidate:
                oldweight = queue.delete(nextnode)
                newweight = min(oldweight, weight)
                queue.insert(nextnode, newweight)

    print ('sum mst: {}'.format(sum(mst)))