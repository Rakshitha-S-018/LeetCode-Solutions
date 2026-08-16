from collections import deque

class Solution:

    def maxDepth(self, root):

        if root is None:
            return 0

        queue = deque([])

        queue.append(root)

        depth = 0

        while len(queue) != 0:

            n = len(queue)

            for i in range(n):

                e = queue.popleft()

                if e.left is not None:
                    queue.append(e.left)

                if e.right is not None:
                    queue.append(e.right)

            depth += 1

        return depth