'''
Generic numeric template formatter
https://www.codewars.com/kata/generic-numeric-template-formatter/python
'''

import string

def numeric_formatter(template, number="1234567890"):

    nformated = ''
    nindex = 0
    
    for ii in range(0,len(template)):
        
        if (template[ii] in string.ascii_letters):
            nformated += number[nindex]
            nindex += 1
            if nindex == len(number):
                nindex = 0
                
        else:
            nformated += template[ii]
    

    return nformated
