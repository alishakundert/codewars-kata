'''
Sum of Cubes
https://www.codewars.com/kata/sum-of-cubes/python
'''

import numpy as np
def sum_cubes(n):
    return np.sum(np.arange(1,n+1)**3)
