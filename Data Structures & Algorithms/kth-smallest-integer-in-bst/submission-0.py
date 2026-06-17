# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: Optional[TreeNode], k: int):
            if not node:
                return None, k
            result, k = dfs(node.left, k)
            if result is not None:
                return result, k
            k -= 1
            if k == 0:
                return node.val, k
            return dfs(node.right, k)
        result, k = dfs(root, k)
        return result