class Solution:

    def solve(self, node):

        if node is None:
            return 0

        LH = self.solve(node.left)
        if LH == -1:
            return -1

        RH = self.solve(node.right)
        if RH == -1:
            return -1

        if abs(LH - RH) > 1:
            return -1

        return 1 + max(LH, RH)

    def isBalanced(self, root):
        return self.solve(root) != -1