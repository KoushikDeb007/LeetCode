# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        node = self.head
        self.ans = []
        while node:
            self.ans.append(node.val)
            node = node.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        # cnt = 0
        # curhead = self.head
        # while(curhead):
        #     cnt +=1
        #     if randint(1, cnt) ==cnt: ans = curhead.val
        #     curhead = curhead.next
        # return ans
        return random.choice(self.ans)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()