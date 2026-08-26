# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not postorder or not inorder:
            return None

        root = TreeNode(postorder[-1])
        
        # postorder[-1] = 3
        mid = inorder.index(postorder[-1])
        

        # Build the LEFT subtree
# inorder[:1] = [9]
# postorder[:1] = [9]
# mid = 1
        root.left = self.buildTree(
            inorder[:mid],
            postorder[:mid]
        )
        

        # Build the RIGHT subtree
# inorder[mid+1:] = inorder[2:] = [15, 20, 7]
# postorder[mid:-1] = postorder[1:-1] = [15, 7, 20]
# mid = 1


        root.right = self.buildTree(
            inorder[mid+1:],
            postorder[mid:-1]
        )

        return root