'''
Sum of odd numbers
https://www.codewars.com/kata/sum-of-odd-numbers/python

Given a triangle of consecutive odd numbers; Calculate the row sums of this triangle from the row index (starting at index 1).
'''

import numpy as np
    
def row_sum_odd_numbers(n):

    # odd number sequence: 2N+1
    N = np.sum(np.arange(0,n)) # starting number on row n
    
    row_arr = [] # will contain elements of row n
    while len(row_arr)<n: # n elements in row n
        row_arr.append((2*N)+1)
        N+=1

    return np.sum(row_arr)
