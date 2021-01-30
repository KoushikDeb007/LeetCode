"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        rethead = head

        def dfs(node):
            next = None
            if node.next:
                next = node.next
            if node.child:
                node.next = node.child
                node.child.prev = node
                temp = node.child
                node.child = None
                child = dfs(temp)
                child.next = next
                if next:
                    next.prev = child
                else:
                    return child
            if not next:
                return node

            return dfs(next)

        if head:
            dfs(head)
        return rethead
