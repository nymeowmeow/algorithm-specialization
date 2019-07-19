def weightjob(jobs):
    wj = sorted(jobs, key = lambda x : (x[0]-x[1], x[0]), reverse = True)
    ct = calculateCompletionTime(wj)
    print ('weight - length, completion time: {}'.format(ct))
    
def ratiojob(jobs):
    wj = sorted(jobs, key = lambda x : x[0]/x[1], reverse = True)
    ct = calculateCompletionTime(wj)
    print ('ratio, completion time: {}'.format(ct))

def calculateCompletionTime(jobs):
    ct = 0
    t = 0
    for j in jobs:
        t += j[1]
        ct += t * j[0]
    return ct


if __name__ == '__main__':
    with open('jobs.txt', 'r') as f:
        next(f)
        jobs = []
        for line in f:
            item = line.strip().split()
            jobs.append((int(item[0]), int(item[1])))
    weightjob(jobs)
    ratiojob(jobs)