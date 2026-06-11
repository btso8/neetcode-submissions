from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            level = []
            for i in range(len(queue)):
                current = queue.pop()
                level.append(current.val)
                if current.left:
                    queue.appendleft(current.left)
                if current.right:
                    queue.appendleft(current.right)
            result.append(level)
        return result