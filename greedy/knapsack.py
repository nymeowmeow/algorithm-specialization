import numpy as np
import copy

if __name__ == '__main__':
    weight = []
    with open('knapsack_big.txt', 'r') as f:
        for i,line in enumerate(f):
            items = line.strip().split()
            if i == 0:
                size = int(items[0])
                count = int(items[1])
            else:
                weight.append((int(items[1]), int(items[0])))
    print ('capacity: {}, count: {}, weight length: {}'.format(size, count, len(weight)))

    #A = np.zeros((len(weight) + 1, size + 1))
    #for i, item in enumerate(weight):
    #    for x in range(size+1):
    #        v = (A[i][x - item[0]] + item[1]) if x  >= item[0] else 0
    #        A[i+1][x] = max(A[i][x], v)
    A = np.zeros(size+1, dtype = int)
    B = np.zeros(size+1, dtype = int)
    for item in weight:
        B[:item[0]] = A[:item[0]]
        for j in range(item[0], size+1):
            B[j] = max(A[j], A[j-item[0]] + item[1])
        A = copy.copy(B)
    print ('max value: {}'.format(A[-1]))
