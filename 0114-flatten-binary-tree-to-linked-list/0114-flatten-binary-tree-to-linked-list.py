# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root):

        if root is None:
            return

        # Store nodes in preorder
        nodes = []

        def preorder(node):
            if node is None:
                return

            nodes.append(node)

            preorder(node.left)
            preorder(node.right)

        preorder(root)

        # Connect nodes using right pointer
        for i in range(len(nodes) - 1):

            nodes[i].left = None
            nodes[i].right = nodes[i + 1]

        # Last node
        nodes[-1].left = None
        nodes[-1].right = None
        