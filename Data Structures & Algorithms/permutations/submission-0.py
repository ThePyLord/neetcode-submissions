class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, perms = [], []

        def dfs(i: int):
            if len(perms) == len(nums):
                res.append(perms[:])
                return
            
            for j in range(len(nums)):
                if nums[j] not in perms:
                    perms.append(nums[j])
                    dfs(i + 1)
                    perms.pop()
            pass
        
        dfs(0)
        return res