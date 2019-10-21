'''
Pyramid Array
https://www.codewars.com/kata/pyramid-array/python
'''

import numpy as np

def pyramid(n):

    pyr = []

    for ii in range(1,n+1):
        pyr.append(list(np.ones(ii,dtype=int)))
        
    return pyr
