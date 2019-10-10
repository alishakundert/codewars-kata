'''
Alphabetical Addition
https://www.codewars.com/kata/alphabetical-addition/python

Description:
Your task is to add up letters to one letter.
The function will be given a variable amount of arguments, each one being a letter to add.
'''

import string

def add_letters(*letters):
    
    alph = string.ascii_lowercase
    
    sumletter = 0
    for letter in letters:
        alphval = alph.find(letter) + 1
        sumletter+=alphval
    
    sumletter = sumletter%26
        
    return alph[sumletter-1]
