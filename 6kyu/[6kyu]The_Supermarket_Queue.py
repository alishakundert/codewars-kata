'''
The Supermarket Queue
https://www.codewars.com/kata/the-supermarket-queue/python
'''

def queue_time(customers, n):

    # single checkout till
    if n == 1:
        return sum(customers)

    # multiple checkout tills
    else:
        dct = {}

        # assign customers to tills
        for index,customer in enumerate(customers):

            # assign first customers in line
            if index in range(0,n):
                dct[str(index)] = customer

            else:
                #check which till is finished first
                # find the till with the min value
                till_min = min(dct.keys(), key=(lambda k: dct[k]))
                dct[str(till_min)] += customer


        # return the maximum value of the tills
        till_max = max(dct.keys(), key=(lambda k: dct[k]))

        return dct[till_max]
