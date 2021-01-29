# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue, result = collections.deque([root]), []
        while (len(queue)):
            size, level = len(queue), []
            for child in range(size):
                par = queue.popleft()
                level.append(par.val)
                if par.left:
                    queue.append(par.left)
                if par.right:
                    queue.append(par.right)
            if len(level):
                result.append(level)

        return result[::-1]