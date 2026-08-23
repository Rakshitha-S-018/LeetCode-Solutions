# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root):
        
        queue = deque()
        
        queue.append((root.left, root.right))
        
        while len(queue) != 0:
            
            node1, node2 = queue.popleft()
            
            # Both nodes are None
            if node1 is None and node2 is None:
                continue
            
            # One is None
            if node1 is None or node2 is None:
                return False
            
            # Values are different
            if node1.val != node2.val:
                return False
            
            # Compare opposite children
            queue.append((node1.left, node2.right))
            queue.append((node1.right, node2.left))
        
        return True