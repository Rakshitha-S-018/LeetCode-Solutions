from collections import deque

class Solution:

    def levelOrder(self, root):
        # Main function called by LeetCode.
        # 'root' is the first node of the tree.

        result = []
        # Store the final answer.
        # Example: [[3],[9,20],[15,7]]

        if root is None:
            # If the tree is empty, return an empty list.
            return result

        queue = deque([])
        # Create an empty queue.

        queue.append(root)
        # Insert the root node into the queue.

        while len(queue) != 0:
            # Repeat until the queue becomes empty.

            level = []
            # Store all node values of the CURRENT LEVEL ONLY.
            # Example:
            # First level -> [3]
            # Second level -> [9,20]
            # Third level -> [15,7]

            n = len(queue)
            # Count how many nodes are present in the current level.
            # Example:
            # queue = [3]      -> n = 1
            # queue = [9,20]   -> n = 2
            # queue = [15,7]   -> n = 2

            for i in range(n):
                # Visit only the nodes of the current level.

                e = queue.popleft()
                # Remove the first node from the queue.

                level.append(e.val)
                # Store the current node value in the current level.
                # NOT in result directly.

                if e.left is not None:
                    
                    queue.append(e.left)

                if e.right is not None:
                    
                    queue.append(e.right)

            result.append(level)
            # Current level is completed.
            # Store it in the final answer.
            # Example:
            # result = [[3]]
            # result = [[3],[9,20]]
            # result = [[3],[9,20],[15,7]]

        return result
       