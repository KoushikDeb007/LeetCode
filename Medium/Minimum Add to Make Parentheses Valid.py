class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        count = 0
        for i in S:
            if i == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    count += 1
                else:
                    stack.pop()
        count += len(stack)
        return count
