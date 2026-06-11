class Solution:
    def isValid(self, s):

        stack = []

        for ch in s:

            if ch in "([{":
                stack.append(ch)

            else:

                if len(stack) == 0:
                    return False

                top = stack.pop() #make sure stack is not empty so we use above 2lines

                if ch == ")" and top != "(":
                    return False

                if ch == "]" and top != "[":
                    return False

                if ch == "}" and top != "{":
                    return False

        if len(stack) == 0:
            return True
        else:
            return False