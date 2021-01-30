# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        deq = collections.deque()
        if root is None:
            return ''
        else:
            deq.appendleft(root)
            s = ''
            while (deq):
                curoot = deq.popleft()
                s = s + '*' + str(curoot.val)
                if curoot.left:
                    deq.append(curoot.left)
                if curoot.right:
                    deq.append(curoot.right)
        return s

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data == '':
            return None
        s = data.split('*')
        s = s[1:]
        # print(s)
        # return ''
        root = TreeNode(int(s[0]))

        for i in range(1, len(s)):
            curroot = root
            val = int(s[i])
            while (curroot):
                if curroot.val > val:
                    if curroot.left:
                        curroot = curroot.left
                    else:
                        curroot.left = TreeNode(val)
                elif curroot.val < val:
                    if curroot.right:
                        curroot = curroot.right
                    else:
                        curroot.right = TreeNode(val)
                else:
                    break
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans