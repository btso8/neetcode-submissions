from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        result = []
        while queue:
            right = None
            for i in range(len(queue)):
                node = queue.pop()
                if node:
                    right = node
                    queue.appendleft(node.left)
                    queue.appendleft(node.right)
            if right:
                result.append(right.val)
        return result