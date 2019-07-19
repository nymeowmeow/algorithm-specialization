import sys

def mergesplit(left, right):
   leftsize = len(left)
   rightsize = len(right)
   i = j = 0
   result = []
   count = 0

   while i < leftsize or j < rightsize:
       if i == leftsize:
           result.extend(right[j:])
           j = rightsize
       elif j == rightsize:
           result.extend(left[i:])
           i = leftsize
       else:
           if left[i] < right[j]:
               result.append(left[i])
               i += 1
           else:
               result.append(right[j])
               j += 1
               count += leftsize - i 

   return count, result

def countinversion(lines):
    if len(lines) == 1:
        return (0, lines)

    mid = len(lines)//2
    leftcount, left = countinversion(lines[:mid])
    rightcount, right = countinversion(lines[mid:])
    splitcount, result = mergesplit(left, right)

    return leftcount + rightcount + splitcount, result
    
if __name__ =='__main__':
    with open('IntegerArray.txt','r') as f:
    #with open('test.txt', 'r') as f:
        lines = [ int(x) for x in f.readlines()]
        print ('number of integers: {}'.format(len(lines)))

        print ('number of inversions: {}'.format(countinversion(lines)[0]))
