'''
Reversing a Process
https://www.codewars.com/kata/reversing-a-process/python
'''

import string
import numpy as np

def decode(r):
    
    alphabet = string.ascii_lowercase

    num = ''
    s = ''
    for ii in range(0,len(r)):

        #character in string is a letter
        if r[ii] in alphabet:

            #solve for x
            arr = np.array([int((x*float(num))%26) for x in range(0,len(alphabet))])
            index = np.where(arr==alphabet.index(r[ii]))[0]

            #if more than two letters meet requirements of x
            if len(index)>1:
                return "Impossible to decode"
         
            s += alphabet[index[0]]


        #character is part of the number prefix
        else: 
            num += r[ii]


    return str(s)
