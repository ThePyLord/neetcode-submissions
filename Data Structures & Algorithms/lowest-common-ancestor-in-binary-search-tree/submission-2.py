# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if root == None:
            # return None

        prev = root
        p, q = min(p.val, q.val), max(p.val, q.val)
        def dfs(root, p, q):
            if not root:
                return None
            if p < root.val and q < root.val:
                return dfs(root.left, p, q)
            elif p > root.val and q > root.val:
                return dfs(root.right, p, q)
            else:
                return root

        lca = dfs(root, p, q)
        return lca
