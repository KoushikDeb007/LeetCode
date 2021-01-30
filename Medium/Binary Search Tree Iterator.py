# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.arr = self.inorder(self.root, [])
        self.pointer = 0

    def next(self) -> int:
        if self.hasNext:
            self.pointer += 1
            return self.arr[self.pointer - 1]

    def hasNext(self) -> bool:
        return self.pointer < len(self.arr)

    def inorder(self, head, path):
        if head:
            self.inorder(head.left, path)
            path.append(head.val)
            self.inorder(head.right, path)
            return path

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()