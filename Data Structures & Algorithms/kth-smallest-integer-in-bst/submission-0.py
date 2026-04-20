# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        k_small = root.val
        def dfs(root: Optional[TreeNode]):
            nonlocal cnt, k_small
            if not root:
                return []
            dfs(root.left)
            if cnt == 1:
                k_small = root.val
            cnt -= 1
            if cnt > 0:
                dfs(root.right)
        
        dfs(root)
        # print(res)
        return k_small