'''
Loose Change
https://www.codewars.com/kata/loose-change/python
'''

def loose_change(cents):

    if cents<0:
        cents = 0
        
    change_dict = {}

    type_arr = ['Quarters', 'Dimes', 'Nickels', 'Pennies']
    value_arr = [25, 10, 5, 1]

    for index, value in enumerate(value_arr):
        change_dict[str(type_arr[index])] = cents//value
        cents = cents%value

    return change_dict
