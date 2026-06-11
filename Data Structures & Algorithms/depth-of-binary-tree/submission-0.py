from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = deque([(root, 1)])
        level = 0
        while stack:
            node, depth = stack.pop()
            if node:
                level = max(depth, level)
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])
        return level