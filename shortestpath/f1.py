import numpy as np

if __name__ == '__main__':
    with open('g2.txt', 'r') as f:
        line = f.readline().strip().split()
        assert(len(line) == 2)
        nodecount = int(line[0].strip())
        edgecount = int(line[1].strip())

        weight = {}
        for line in f:
            item = line.strip().split()
            n1   = int(item[0].strip())
            n2   = int(item[1].strip())
            w    = int(item[2].strip())
            weight[(n1, n2)] = w

        print ('node count: {}, edge count: {}, edge size: {}'.format(nodecount, edgecount, len(weight)))
        BIG = 99999999
        A = np.ones((nodecount+1, nodecount+1)) * BIG
        for i in range(nodecount+1):
            for j in range(nodecount + 1):
                if i == j:
                   A[i,j] = 0
                elif (i,j) in weight:
                   A[i,j] = weight[(i,j)]

        for k in range(1, nodecount+1):
            for i in range(1, nodecount+1):
                for j in range(1, nodecount+1):
                    A[i,j] = min(A[i,j], A[i,k] + A[k, j])
                    if i == j and A[i,j] < 0:
                        raise ValueError('negative cycle detected')
        print ('min is : {}'.format(np.min(np.min(A, axis = 1))))

