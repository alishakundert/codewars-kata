'''
Tree to list
https://www.codewars.com/kata/tree-to-list/python
'''

class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes

def tree_to_list(tree_root):

    treelist = [tree_root.data]
    subnodes = [tree_root.child_nodes]
    
    while subnodes != []:
        
        subnodes_new = []
        for subnode in subnodes:
            if subnode is None:
                continue
            treelist += [x.data for x in subnode]
            subnodes_new += [x.child_nodes for x in subnode]

        subnodes = subnodes_new

    return treelist
