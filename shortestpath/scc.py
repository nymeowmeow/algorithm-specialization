import sys
from collections import defaultdict

class GraphInfo(object):
    def __init__(self):
        self.explored = set()
        self.processed = set()
        self.currentsource = 0
        self.leader = defaultdict(set)
        self.finishtime = []
        self.currenttime = 0

def dfs(node, edges, info):
    stack = [ node ]
    while stack:
        current = stack[-1]
        if current in info.explored:
            current = stack.pop()
            if current not in info.processed:
                info.currenttime += 1
                info.finishtime.append((info.currenttime, current))
                info.processed.add(current)
        else: #first see the node
            info.explored.add(current)
            info.leader[info.currentsource].add(current)

            for item in edges[current]:
                if item not in info.explored and item not in info.processed:
                    stack.append(item)

def dfs_loop(nodelist, edges):
    info = GraphInfo()
    for node in nodelist:
        if node not in info.explored:
            info.currentsource = node
            dfs(node, edges, info)

    return info.finishtime, info.leader

def getssc(edges, reverseEdges):
    #perform dfs on reverseGraph, find the corresponding finishing time
    nodes = sorted(edges.keys(), reverse = True)
    finishtime, leader = dfs_loop(nodes, reverseEdges)

    #use finishing time to find the list of scc
    finishtime = sorted(finishtime, reverse = True)
    ordernode = [ n for (t, n) in finishtime ]
    _, leader = dfs_loop(ordernode, edges)

    sccsize = sorted([ (len(v), k) for (k,v) in leader.items() ], reverse = True)
    return sccsize

def getssc1(edges, reverseEdges):
    #perform dfs on reverseGraph, find the corresponding finishing time
    nodes = sorted(edges.keys(), reverse = True)
    finishtime, leader = dfs_loop(nodes, reverseEdges)

    #use finishing time to find the list of scc
    finishtime = sorted(finishtime, reverse = True)
    ordernode = [ n for (t, n) in finishtime ]
    _, leader = dfs_loop(ordernode, edges)

    return leader

if __name__ == '__main__':
    edges = defaultdict(list)
    reverseEdges = defaultdict(list)
    with open('scc.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            n = line.strip().split()
            assert(len(n) == 2)
            n1 = int(n[0])
            n2 = int(n[1])
            edges[n1].append(n2)
            if n2 not in edges:
                edges[n2] = []
            reverseEdges[n2].append(n1)
            if n1 not in reverseEdges:
                reverseEdges[n1] = []
 
    scc = getssc(edges, reverseEdges)
    print ([ g[0] for g in scc[:10]])
