class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare
        # s = set()
        # for i in nums:
        #     if i in s:
        #         return i
        #     s.add(i)
        # for i in nums:
        #     if nums[abs(i)]<0:
        #         return abs(i)
        #     else:
        #         nums[abs(i)]= -nums[abs(i)]

