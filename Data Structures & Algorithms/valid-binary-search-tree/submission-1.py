# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], high: int, low: int) -> bool:
            if not node:
                return True
            if node.val >= high or node.val <= low:
                return False
            else:
                return dfs(node.left, node.val, low) and dfs(node.right, high, node.val)        
        return dfs(root, float("inf"), float("-inf"))