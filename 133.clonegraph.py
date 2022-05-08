"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        #0. take care of corner case
        if (node is None):
            return None

        oldToNew = {}
    
        def clone(node):
            #1. check if it's already in hashmap
            if (node in oldToNew):
                return oldToNew[node]
            
            #2. clone value and put it into hashmap 
            copy = Node(node.val)
            oldToNew[node] = copy
                
            #3. clone all the neighbors recursively    
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy
            
        return clone(node)
