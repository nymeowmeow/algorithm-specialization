from scc import getssc1
from collections import defaultdict

if __name__ == '__main__':
    result = []
    for i in range(1, 7):
        filename = '2sat{}.txt'.format(i)
        with open(filename, 'r') as f:
            clausecount = int(f.readline().strip())
            print ('{}: clausecount: {}'.format(filename, clausecount))
            edges = defaultdict(list)
            reverseEdges = defaultdict(list)
            for line in f:
                item = line.strip().split()
                x1 = int(item[0])
                x2 = int(item[1])

                edges[-x1].append(x2)
                reverseEdges[x2].append(-x1)
                if x2 not in edges:
                    edges[x2] = []
                if -x1 not in reverseEdges:
                    reverseEdges[-x1] = []
                edges[-x2].append(x1)
                reverseEdges[x1].append(-x2)
                if x1 not in edges:
                    edges[x1] = []
                if -x2 not in reverseEdges:
                    reverseEdges[-x2] = []

            leaders = getssc1(edges, reverseEdges)
            ok = True
            for group in leaders.values():
                group = set(group)
                for node in group:
                    if -node in group:
                        ok = False
                        break
            result.append(0 if not ok else 1)
            print ('file ', filename, result)
    print (result)
