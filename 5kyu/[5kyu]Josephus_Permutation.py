'''
Josephus Survivor
https://www.codewars.com/kata/josephus-survivor/python

In this kata you have to correctly return who is the "survivor", ie: the last element of a Josephus permutation.

Basically you have to assume that n people are put into a circle and that they are eliminated in steps of k elements. 

You may assume that both n and k will always be >=1.
'''

import numpy as np
def josephus_survivor(n,k):

    # initial list sequence
    lst = list(np.arange(1,n+1))
    print(lst)
    
    start_index = -1
    while len(lst)>1:

        while start_index+k>=len(lst):
            start_index=start_index-len(lst)

        # eliminating element from list
        lst.pop(start_index+k)
        
        start_index = start_index+k-1

        print(lst)

    return lst[0]


