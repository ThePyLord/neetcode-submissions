# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root: Optional[TreeNode]):
            q = deque([root])
            res = []

            while q:
                q_len = len(q)
                last = None
                for i in range(q_len):
                    node = q.popleft()
                    if node:
                        last = node
                        q.append(node.left)
                        q.append(node.right)
                if last:
                    res.append(last.val)
            return res
        
        return bfs(root)