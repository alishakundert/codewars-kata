'''
Bingo ( Or Not )
https://www.codewars.com/kata/bingo-or-not/python
'''

import string

def bingo(array):

    alphabet = string.ascii_uppercase

    newstring = ''
    for number in array:
        newstring = newstring+str(alphabet[number-1])

    for ii in range(0,len('BINGO')):
        if 'BINGO'[ii] in newstring:
            continue
        else:
            return 'LOSE'

    return 'WIN'

