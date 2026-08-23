# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p, q):

        queue = deque()

        queue.append((p, q))

        while len(queue) != 0:

            node1, node2 = queue.popleft()

            # Both nodes are None
            if node1 is None and node2 is None:
                continue

            # One is None or values are different
            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False

            # Add left children
            queue.append((node1.left, node2.left))

            # Add right children
            queue.append((node1.right, node2.right))

        return True