'''
Rotate for a Max
https://www.codewars.com/kata/rotate-for-a-max/python
'''

def max_rot(n):

    rot_arr = [n]

    ns = str(n) 
    for ii in range(0,len(str(n))-1):

        ns = ns[:ii]+ns[ii+1:]+ns[ii]
        rot_arr.append(int(ns))
        
 
    return max(rot_arr)
