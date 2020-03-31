'''
Best travel
https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/python
'''

import numpy as np
from itertools import combinations 

def choose_best_sum(t, k, ls):

    # all possible combinations
    comb = combinations(ls, k)
    
    # compute sum of all combinations
    sum_comb = np.array(list(set([sum(p) for p in comb])))

    # reduce sums to max cutoff
    sum_comb = sum_comb[sum_comb<=t]

    if len(sum_comb) == 0:
        # minimum sum of distances greater than cutoff
        return None

    else:
        # return maximum sum of combinations 
        return max(sum_comb)
