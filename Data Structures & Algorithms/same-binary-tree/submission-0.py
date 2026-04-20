# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(root: Optional[TreeNode]):
            q = deque([root])
            res = []
            while q:
                node = q.popleft()
                if not node:
                    res.append(None)
                    continue
                q.append(node.left)
                q.append(node.right)
                res.append(node.val)
            return res

        return bfs(p) == bfs(q)