'''
Simple Fun #2: Circle of Numbers
https://www.codewars.com/kata/simple-fun-number-2-circle-of-numbers/python

Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighbouring numbers is equal (note that 0 and n - 1 are neighbouring, too).

Given n and firstNumber/first_number, find the number which is written in the radially opposite position to firstNumber.
'''

def circle_of_numbers(n, fst):
    if fst < n/2.:
        return fst + n/2.
    else:
        return fst - n/2.
