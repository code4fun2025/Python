class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

       
        def dfs(node, minVal, maxVal):
            if not node:
                return True
            
            if  node.val <= minVal or node.val >= maxVal:
                return False
            
            
            return dfs(node.left, minVal, node.val) and dfs(node.right, node.val, maxVal)

        return dfs(root, float('-inf'), float('+inf'))          
