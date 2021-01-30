class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        flag = 1
        for i in range(len(nums)):
            # res[-1] = nums[i]
            while stack and stack[-1][0] < nums[i]:
                res[stack[-1][1]] = nums[i]
                stack.pop()
            # if i != len(nums)-1:
            stack.append((nums[i], i))

        for i in range(len(nums)):
            if not stack:
                break
            while (stack and stack[-1][0] < nums[i]):
                res[stack[-1][1]] = nums[i]
                stack.pop()
        return res