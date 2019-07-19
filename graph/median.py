import heapq

if __name__ == '__main__':
    input = []
    with open('median.txt', 'r') as f:
        for line in f:
            input.append(int(line.strip()))

    print ('number of input elements: {}'.format(len(input)))
    heapmin = []
    heapmax = []
    heapq.heapify(heapmin)
    heapq.heapify(heapmax)

    total = 0
    for item in input:
        if len(heapmax) == 0:
            heapq.heappush(heapmax, -item)
        else:
            maxvalue = -heapmax[0] #get the max value of the max heap
            if item > maxvalue:
                #insert to min heap
                heapq.heappush(heapmin, item)
                if len(heapmin) > len(heapmax):
                    minvalue = heapq.heappop(heapmin)
                    heapq.heappush(heapmax, -minvalue)
            else:
                heapq.heappush(heapmax, -item)
                if len(heapmax) - len(heapmin) > 1:
                    maxvalue = -heapq.heappop(heapmax)
                    heapq.heappush(heapmin, maxvalue)
        median = -heapmax[0]
        total  = (total + median) % 10000
    print ('total is {}'.format(total))