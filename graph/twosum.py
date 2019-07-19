import bisect

if __name__ == '__main__':
    input = []
    with open('algo1-programming_prob-2sum.txt', 'r') as f:
        for line in f:
            input.append(int(line.strip()))
    input.sort()
    print ('number of input: {}'.format(len(input)))
    bound = 10000
    result = set()
    for i in input:
       lowerbound = bisect.bisect_left(input, -bound - i)
       upperbound = bisect.bisect_right(input, bound - i)
       candidate = [ i + j for j in input[lowerbound:upperbound] ]
       result.update(candidate)

    print (len(result))
