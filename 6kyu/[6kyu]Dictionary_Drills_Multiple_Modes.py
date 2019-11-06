'''
Thinkful - Dictionary Drills: Multiple Modes
https://www.codewars.com/kata/thinkful-dictionary-drills-multiple-modes/python
'''

def modes(data):

    #put data into dictionary
    dict = {}
    for char in data:
        dict[char] = dict.get(char, 0) + 1

    #identify modes
    mode_list = [k for k, v in dict.items() if v==max(dict.values())]
    mode_list.sort()
    
    #handle cases of no mode
    if len(mode_list)==len(dict):
        mode_list = []
        
    return mode_list
