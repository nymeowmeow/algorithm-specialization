import sys
    
def quicksort(lines, start, end, choosepivot):
    if end <= start+1:
        return 0

    pivot = choosepivot(lines, start, end)
    pivotvalue = lines[pivot]
    #swap start with pivot
    if pivot != start:
        lines[start], lines[pivot] = lines[pivot], lines[start] #swap pivot with first element

    i = j = start + 1
    while j < end:
        if lines[j] < pivotvalue:
            lines[j], lines[i] = lines[i], lines[j]
            i += 1
        j += 1

    lines[start], lines[i-1] = lines[i-1], lines[start]
    pivot = i - 1
    left = quicksort(lines, start, pivot, choosepivot) 
    right = quicksort(lines, pivot+1, end, choosepivot)

    return left + right + (end - start - 1)


#choose first element in range to be the pivot
def firstelement(lines, start, end):
    return start

def lastelement(lines, start, end):
    return end - 1

def medianelement(lines, start, end):
    firstvalue = lines[start]
    lastvalue = lines[end - 1]
    length = end - start
    middle = start + length//2
    if length % 2 == 0:
       middle -= 1
    middlevalue = lines[middle]
    index = middle # firstvalue < middlevalue < lastvalue or lastvalue < middlevalue < firstvalue
    if (firstvalue < lastvalue < middlevalue) or (middlevalue < lastvalue < firstvalue):
       middle = end - 1
    elif (middlevalue < firstvalue < lastvalue) or (lastvalue < firstvalue < middlevalue):
       middle = start

    return middle

if __name__ =='__main__':
    with open('quicksort.txt','r') as f:
    #with open('test.txt', 'r') as f:
        lines = [ int(x) for x in f.readlines()]
        print ('number of integers: {}'.format(len(lines)))

        print ('number of comparsions: {}'.format(quicksort(lines, 0, len(lines), medianelement)))
