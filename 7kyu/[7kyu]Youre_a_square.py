'''
You're a square!
https://www.codewars.com/kata/youre-a-square/python
'''

import numpy as np

def is_square(n):

    if np.isnan(np.sqrt(n))==True:
        return False
    elif (np.sqrt(n)==int(np.sqrt(n))):
        return True
    else:
        return False
    
