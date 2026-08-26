class Solution:
    def buildTree(self, preorder, inorder):

        # If there are no elements, there is no tree
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        # Find the root's position in inorder
        #
        # inorder = [9, 3, 15, 20, 7]
        #                 ↑
        #                root
        #
        # inorder.index(3) = 1
        #
        # So:
        # elements before index 1  → LEFT subtree
        # elements after index 1   → RIGHT subtree
        mid = inorder.index(preorder[0])

        # Build the LEFT subtree
        #preorder[1:2] = [9]
        #inorder[:1] = [9]
        
        root.left = self.buildTree(
            preorder[1:mid + 1],
            inorder[:mid]
        )

        # Build the RIGHT subtree
        
        # inorder[mid + 1:]
        # →preorder[2:] = [20, 15, 7]
        #inorder[2:] = [15, 20, 7]
        
        root.right = self.buildTree(
            preorder[mid + 1:],
            inorder[mid + 1:]
        )

        return root