'''
Growing Plant
https://www.codewars.com/kata/simple-fun-number-74-growing-plant/python
'''

def growing_plant(upSpeed, downSpeed, desiredHeight):

    day = 1
    height = 0
    while height < desiredHeight:
        
        height += upSpeed #day
        if height >= desiredHeight:
            break
        else:
            height -= downSpeed #night
            
        day += 1

    return day
