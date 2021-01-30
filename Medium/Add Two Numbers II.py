# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i = 10
        first = 0
        while l1:
            first = i*first + l1.val
            l1 = l1.next
            # i*=10
        i ,second = 10,0
        while l2:
            second = i*second + l2.val
            l2 = l2.next
            # i*=10
        # print(first,second)
        total = str(first + second)
        total = total[::-1]
        newlist = ListNode(int(total[0]))
        total = total[1:]
        for val in total:
            newNode = ListNode(int(val),newlist)
            newlist = newNode
        return newlist