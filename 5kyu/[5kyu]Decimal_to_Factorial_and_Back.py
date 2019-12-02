'''
Decimal to Factorial and Back
https://www.codewars.com/kata/decimal-to-factorial-and-back/python
'''

import string
from math import factorial

def dec2FactString(nb):

    alph = string.ascii_uppercase
    digitlst = list(range(0,10)) + list(alph)
    
    faclst = [factorial(x) for x in range(0,len(digitlst)) if factorial(x) < nb]

    s = ''
    while len(faclst) > 0:
        s += str(digitlst[nb//faclst[-1]])
        nb = nb % faclst.pop(-1)

    return s


def factString2Dec(s):

    alph = string.ascii_uppercase
    digitlst = [str(x) for x in range(0,10)] + list(alph)
    
    lst = [digitlst.index(x) for x in list(s)]

    nb = 0
    while len(lst) > 0:
        nb += lst.pop(0)*factorial(len(lst))

    return int(nb)
