# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def func(rt):
            if not rt:
                return rt
            if low <= rt.val <= high:
                rt.left = func(rt.left)
                rt.right = func(rt.right)
            elif rt.val < low:
                rt = func(rt.right)
            elif rt.val > high:
                rt = func(rt.left)
            return rt

        return func(root)