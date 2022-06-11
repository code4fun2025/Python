class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                nextNode = root.right
                while nextNode.left:
                    nextNode = nextNode.left
                root.val = nextNode.val
                nextNode.val = key
                root.right = self.deleteNode(root.right, key)
            # the node is not a leaf, has no right child, and has a left child    
            else:
                nextNode = root.left
                while nextNode.right:
                    nextNode = nextNode.right
                root.val = nextNode.val
                nextNode.val = key
                root.left = self.deleteNode(root.left, key)
                        
        return root
