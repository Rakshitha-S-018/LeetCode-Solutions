# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
# Import deque so we can create a queue.


class Solution:
    def hasPathSum(self, root, targetSum):

        # If the tree is empty, there is no root-to-leaf path.
        if root is None:
            return False

        # Create an empty queue.
        queue = deque()

        # Store:
        # 1. The current node
        # 2. The sum of the path from root to that node
        #
        # Initially, we are at the root,
        # so the sum is root.val.
        queue.append((root, root.val))

        # Continue until the queue becomes empty.
        while len(queue) != 0:

            # Remove the first pair from the queue.
            #
            # Example:
            # (5, 5)
            # means:
            # node = 5
            # current_sum = 5
            node, current_sum = queue.popleft()

            # Check whether the current node is a leaf.
            #
            # A leaf has:
            # no left child
            # AND
            # no right child
            if node.left is None and node.right is None:

                # If this root-to-leaf path has the required sum,
                # we found the answer.
                if current_sum == targetSum:
                    return True

            # If a left child exists...
            if node.left is not None:

                # Add the left child to the queue.
                #
                # Also calculate the new path sum:
                #
                # old sum + left child's value
                #
                # Example:
                # current_sum = 5
                # left child = 4
                #
                # new sum = 5 + 4 = 9
                queue.append(
                    (node.left, current_sum + node.left.val)
                )

            # If a right child exists...
            if node.right is not None:

                # Add the right child to the queue.
                #
                # New path sum:
                #
                # old sum + right child's value
                queue.append(
                    (node.right, current_sum + node.right.val)
                )

        # We checked every root-to-leaf path
        # and none had the target sum.
        return False