# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            root = TreeNode(val)
            return root

        else:
            curroot = root
            while (True):
                if curroot.val > val:
                    if curroot.left:
                        curroot = curroot.left
                    else:
                        curroot.left = TreeNode(val)
                        return root
                else:
                    if curroot.val < val:
                        if curroot.right:
                            curroot = curroot.right
                        else:
                            curroot.right = TreeNode(val)
                            return root

