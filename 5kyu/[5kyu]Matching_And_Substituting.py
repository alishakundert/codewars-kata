'''
Matching And Substituting
https://www.codewars.com/kata/matching-and-substituting/python
'''

def change(s, prog, version):

    s=s.split('\n')
    dct = dict([s[i].split(': ') for i in range(0,len(s))])

    # replace title with prog
    del dct['Program title']
    dct['Program'] = str(prog)

    # change date to '2019-01-01'
    dct['Date'] =  '2019-01-01'

    # change author to 'g964'
    dct['Author'] = 'g964'

    # remove corporation and level
    del dct['Corporation']
    del dct['Level']

    #check if phone is of correct format
    testphone = dct['Phone'].split('-')
    if ([len(x) for x in testphone]!=[2, 3, 3, 4]) | (testphone[0]!='+1'):
        return "ERROR: VERSION or PHONE"
    else:
        dct['Phone'] = "+1-503-555-0090"

    # check if version is of correct format
    testversion = dct['Version'].split('.')
    if (len(testversion)!=2) | ('' in testversion):
        return "ERROR: VERSION or PHONE"
    if dct['Version'] != '2.0':
        dct['Version'] = str(version)
        
    # reformat dictionary to string
    return " ".join("{}: {}".format(key, dct[key]) for key in ['Program','Author','Phone','Date','Version'])
