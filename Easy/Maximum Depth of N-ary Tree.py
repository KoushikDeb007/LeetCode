# Given a n-ary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along
# the longest path from the root node down to the farthest leaf node.
# Nary-Tree input serialization is represented in their level order
# traversal, each group of children is separated by the null value.

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


        ##########  recursive approach ########
import collections


class SolutionNo1:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        mv = 0
        for child in root.children:
            mv = max(mv, self.maxDepth(child))
        return 1 + mv


        ########## BFS APPROACH ##########

class SolutionNo2:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0

        mdepth = 1
        queue = collections.deque([(root, 1)])

        while (len(queue)):
            par, depth = queue.popleft()
            for child in par.children:
                queue.append((child, depth + 1))
            mdepth = max(mdepth, depth)
        return mdepth

