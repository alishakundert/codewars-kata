'''
Plus - minus - plus - plus - ... - Count
https://www.codewars.com/kata/plus-minus-plus-plus-dot-dot-dot-count/python

Count how often sign changes in array.
'''

def catch_sign_change(lst):
    count = 0

    # check if list element is the same sign as the previous element
    for ii in range(1,len(lst)):

        if ((lst[ii]>=0)&(lst[ii-1]>=0)) | ((lst[ii]<0)&(lst[ii-1]<0)):
            pass
            
        else:
            # change in sign identified
            count+=1
        
    return count
