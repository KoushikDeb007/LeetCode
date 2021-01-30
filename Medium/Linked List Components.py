# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        s = set(G)
        res = 1
        prev = False
        while (head):
            if not s:
                break
            if s and prev and head.val not in s:
                res += 1
                prev = False
            elif head.val in s:
                s.remove(head.val)
                prev = True
            head = head.next

        return res