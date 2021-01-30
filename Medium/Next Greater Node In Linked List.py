# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []

        count = 0
        chead = head
        while (chead):
            count += 1
            chead = chead.next

        res = [0] * count
        chead = head
        count = 0
        while (chead):
            while stack and stack[-1][1] < chead.val:
                res[stack.pop()[0]] = chead.val
            stack.append((count, chead.val))
            count += 1
            chead = chead.next
        return res
