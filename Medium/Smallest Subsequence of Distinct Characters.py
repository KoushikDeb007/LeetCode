class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        d = Counter(s)
        for ch in s:
            d[ch] -= 1
            if ch not in stack:
                while stack and stack[-1] > ch and d[stack[-1]]:
                    stack.pop()
                stack.append(ch)

        return ''.join(stack)
