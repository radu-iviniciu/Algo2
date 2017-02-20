""" 1. In this programming problem and the next you'll
code up the greedy algorithms from lecture for minimizing the weighted sum of completion times..

Download the text file below.

jobs.txt
This file describes a set of jobs with positive and integral weights and lengths. It has the format

[number_of_jobs]

[job_1_weight] [job_1_length]

[job_2_weight] [job_2_length]

...

For example, the third line of the file is "74 59",
indicating that the second job has weight 74 and length 59.

You should NOT assume that edge weights or lengths are distinct.

Your task in this problem is to run the greedy algorithm that
schedules jobs in decreasing order of the difference (weight - length).
Recall from lecture that this algorithm is not always optimal. IMPORTANT: if two jobs
have equal difference (weight - length), you should schedule the job with higher
weight first. Beware: if you break ties in a different way, you are likely to get
the wrong answer. You should report the sum of weighted completion times of the resulting
schedule --- a positive integer --- in the box below.

ADVICE: If you get the wrong answer, try out some small test
cases to debug your algorithm (and post your test cases to the discussion forum).

P2. For this problem, use the same data set as in the previous problem.

Your task now is to run the greedy algorithm that schedules jobs (optimally) in 
decreasing order of the ratio (weight/length). In this algorithm, it does not matter 
how you break ties. You should report the sum of weighted completion times of the resulting schedule
 --- a positive integer --- in the box below. """
from pprint import *

def greedy_unoptimal(jobs):
    return sorted(jobs, key = lambda j: ((j[0] - j[1]), j[0]), reverse = True)

def greedy_optimal(jobs):
    return sorted(jobs, key = lambda j: ((j[0] / j[1])), reverse = True)

def completion_times(jobs):
    result = list()    
    for j in jobs:
        if any(result):
            result.append(result[-1] + j)
        else:
            result.append(j)
    return result            

def wcs(jobs, greedy):
    """ Weighted Completion Times sum for jobs.
    Jobs: [(w,l),...] - list of jobs (weight and length)
    greedy: function for greedy sorting this list (takes in jobs as parameter)

    Returns: Sum of weighted completion times
    """ 
    sort = greedy(jobs)
    cp = completion_times([l for w,l in sort])

    weightAndCompletion = zip([w for w,l in sort], cp)
    weightedCompletion = sum(w*c for w,c in weightAndCompletion)
    return weightedCompletion

from utils import *

if __name__ == "__main__":
    lines = read_lines("jobs.txt")
    n = int(lines[0])
    jobs = [tuple(int (x) for x in l.split(' ')) for l in lines[1:]]

    p1_wcs = wcs(jobs, greedy_unoptimal)

    p2_wcs = wcs(jobs, greedy_optimal)

    pprint("P1. Unoptimal greedy algo Sum(w*c): " + str(p1_wcs))
    pprint("P2. OPtimal greedy algo Sum(w*c): " + str(p2_wcs))