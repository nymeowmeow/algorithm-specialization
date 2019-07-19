import heapq

if __name__ == '__main__':
    weight = []
    with open('huffman.txt', 'r') as f:
        count = int(f.readline().strip())
        for line in f:
            weight.append(int(line.strip()))

    print ('count : {}, weight count: {}'.format(count, len(weight)))
    heap = [ (w, str(i), 0, 0) for i,w in enumerate(weight) ]
    heapq.heapify(heap)
    while len(heap) != 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        combined = ( first[0] + second[0], first[1] + second[1], max(first[2], second[2]) + 1, min(first[3], second[3]) + 1)
        heapq.heappush(heap, combined)
    root = heapq.heappop(heap)
    print (root[2], root[3])