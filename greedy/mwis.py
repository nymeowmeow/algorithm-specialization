if __name__ == '__main__':
    path = []
    with open('mwis.txt', 'r') as f:
        nodecount = int(f.readline().strip())
        for line in f:
            path.append(int(line.strip()))
    print ('node count: {}, path: {}'.format(nodecount, len(path)))

    target = [ 1, 2, 3, 4, 17, 117, 517, 997]
    A = [ 0, path[0] ]
    for i in range(2, len(path) + 1):
        A.append(max(A[i-1], A[i-2] + path[i-1]))

    result = []
    i = len(A) - 1
    while i > 1:
        if A[i-1] >= A[i-2] + path[i-1]:
            i -= 1
        else:
            result.append(i)
            i -= 2
    if i == 1:
        result.append(1)

    print ([ value in result for value in target])