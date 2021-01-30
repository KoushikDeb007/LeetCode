class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if len(T) == 1:
            return [0]
        retlist = [0] * len(T)
        stack = [(0, T[0])]

        for i in range(1, len(T)):
            while stack and stack[-1][1] < T[i]:
                popped = stack.pop()
                retlist[popped[0]] = i - popped[0]
            stack.append((i, T[i]))
        return retlist
