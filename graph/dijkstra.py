import heapq

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

def dijkstra(s, queue, edges):
    size = len(queue.heap) + 1
    processed = [ s ]
    candidate = set([i[1] for i in queue.heap])
    shortestPath = {}
    shortestPath[s] = 0

    while size > len(processed):
        (min_dist, node) = queue.pop()
        processed.append(node)
        candidate.remove(node)
        shortestPath[node] = min_dist
        for n, dist in edges[node]:
            if n in candidate:
                old_dist = queue.delete(n)
                new_dist = min(old_dist, min_dist + dist)
                queue.insert(n, new_dist)
    return shortestPath
            
if __name__ == '__main__':
   INFINITY = 1000000
   graph = {}
   nodeset = set()
   with open('dijkstraData.txt', 'r') as f:
       for line in f:
          c = line.strip().split()
          node = int(c[0])
          nodeset.add(node)
          edge = [ (int(k.split(',')[0]), int(k.split(',')[1])) for k in c[1:] ]
          for item in edge:
              nodeset.add(item[0])
          graph[node] = edge
   print ('number of nodes: {}'.format(len(graph)))
   target = [ 7,37,59,82,99,115,133,165,188,197]
   nodelist = graph.keys()
   for node in nodelist:
       for (n, dist) in graph[node]:
           if n not in graph:
               graph[n] = [ (node, dist) ]
           if (node, dist) not in graph[n]:
               graph[n].append((node, dist))
   s = 1
   heap = []
   sourcedict = dict(graph[s])
   for n in list(nodeset):
       if n == s:
          continue
       if n in sourcedict:
          heap.append([sourcedict[n], n])
       else:
          heap.append([INFINITY, n])
   queue = PriorityQueue(heap)
   distance = dijkstra(s, queue, graph)
   print ([ distance[i] for i in target ])


          