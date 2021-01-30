class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        stacklen = 0
        slen = len(s)
        for i in range(slen):
            if s[i] == '(':
                stack.append((i, s[i]))
                stacklen += 1
            elif s[i] == ')':
                if stacklen and stack[-1][1] == '(':
                    stack.pop()
                    stacklen -= 1
                else:
                    stack.append((i, s[i]))
                    stacklen += 1
        # slist = [char for char in s]
        if stacklen == 0:
            return s
        result = s[:stack[0][0]]
        for i in range(1, stacklen):
            result += s[stack[i - 1][0] + 1:stack[i][0]]
        result += s[stack[-1][0] + 1:]
        return result
