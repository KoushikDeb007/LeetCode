# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        total = 0
        cur = head
        while (cur):
            total += 1
            cur = cur.next
        ind = 0
        cur = head
        first, second = None, None
        # print(total)
        while (cur):
            if ind == k - 1:
                first = cur
            if ind == total - k:
                second = cur
            ind += 1
            cur = cur.next

        first.val, second.val = second.val, first.val
        return head
