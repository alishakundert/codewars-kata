'''
Directions Reduction
https://www.codewars.com/kata/directions-reduction/python
'''

def opp(s):
    if s == 'NORTH':
        return 'SOUTH'
    elif s == 'SOUTH':
        return 'NORTH'
    elif s == 'EAST':
        return 'WEST'
    elif s == 'WEST':
        return 'EAST'

def dirReduc(arr):
    
    while True:
    
        keepind = [i for i in range(0,len(arr))]

        for ii in range(0,len(arr)-1):
            
            if ii not in keepind:
                continue
            
            if arr[ii+1] == opp(arr[ii]):
                keepind.remove(ii)
                keepind.remove(ii+1)
            
        if len(arr) == len(keepind):
            break
        
        arr = [arr[i] for i in keepind]
        
    return arr
