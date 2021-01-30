# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head and head.next:
            first= head
            second,even = head.next,head.next
            counter,count = head.next.next,1
            while(counter):
                if count==1:
                    first.next = counter
                    count = 2
                    first = first.next
                else:
                    second.next = counter
                    count = 1
                    second = second.next
                counter = counter.next
            first.next = even
            second.next = None
        return head