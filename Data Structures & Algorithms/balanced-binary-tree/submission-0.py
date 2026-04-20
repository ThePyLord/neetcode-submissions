# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        l_depth = self.dfs(root.left)
        r_depth = self.dfs(root.right)
        balanced = abs(l_depth - r_depth) <= 1
        if not balanced: 
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
		
    def dfs(self, node: Optional[TreeNode]):
        if not node:
            return 0
        return max(self.dfs(node.left), self.dfs(node.right)) + 1