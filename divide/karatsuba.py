import sys
import math

def pad(data, length):
    return data.zfill(length)

def karatsuba(first, second):
    # make sure operand are of the same length
    if first < 10 and second < 10:
        return first * second

    firststr = str(first)
    secondstr = str(second)
    length = max(len(firststr), len(secondstr))
    firststr = pad(firststr, length)
    secondstr = pad(secondstr, length)
    mid = length//2
    print ('enter', firststr, secondstr, mid)

    b = int(firststr[:mid])
    a = int(firststr[mid:])
    d = int(secondstr[:mid])
    c = int(secondstr[mid:])

    z0 = karatsuba(a, c)
    z1 = karatsuba((a + b), (c + d))
    z2 = karatsuba(b, d)

    factor = math.ceil(length/2)
    print ('z0', z0, z1, z2, mid)
    res = (z2 * 10**(2 * factor)) + ((z1 - z2 - z0) * 10**factor) + z0
    return res
 
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print ('expecting 2 arguments, instead get {}'.format(len(sys.argv) - 1))
        sys.exit(-1)

    first = sys.argv[1]
    second = sys.argv[2]
    if not (first.isnumeric() and second.isnumeric()):
       print ('number expected to be numeric, instead get {} and {}'.format(first, second));
       sys.exit(-1)

    result = karatsuba(int(first), int(second))
    print ('{} * {} = {}'.format(first, second, result))
        