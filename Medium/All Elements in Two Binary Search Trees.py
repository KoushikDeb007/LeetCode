# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        res = []

        def app(root):
            # while(root):
            if root:
                res.append(root.val)
                app(root.left)
                app(root.right)

        app(root1)
        app(root2)
        res.sort()
        return res