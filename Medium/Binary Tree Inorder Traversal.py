# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #         res = []
        #         def inord(root):
        #             if root:
        #                 inord(root.left)
        #                 res.append(root.val)
        #                 inord(root.right)

        #         inord(root)
        #         return res
        res = []
        cur = root
        if not root:
            return res

        stack = []
        while stack or cur:
            while (cur):
                stack.append(cur)
                cur = cur.left
            if stack:
                res.append(stack[-1].val)
                cur = stack.pop().right

        return res
