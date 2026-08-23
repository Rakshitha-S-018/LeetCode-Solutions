# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def sumNumbers(self, root):

        # Create a queue.
        # Store:
        # (node, number formed from root to this node)
        queue = deque()

        # Start with the root.
        queue.append((root, root.val))

        # This will store the total of all root-to-leaf numbers.
        total = 0

        while len(queue) != 0:

            # Remove the first node and its current number.
            node, current_num = queue.popleft()

            # If this is a leaf,
            # current_num is a complete root-to-leaf number.
            if node.left is None and node.right is None:
                total += current_num

            # If left child exists,
            # append its digit to the current number.
            if node.left is not None:

                new_num = current_num * 10 + node.left.val

                queue.append((node.left, new_num))

            # If right child exists,
            # append its digit to the current number.
            if node.right is not None:

                new_num = current_num * 10 + node.right.val

                queue.append((node.right, new_num))

        return total
        