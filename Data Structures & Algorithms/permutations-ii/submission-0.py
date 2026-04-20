class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, perms = set(), []

        def dfs(subset: List[int]):
            if len(perms) == len(nums):
                res.add(tuple(perms))
                return
            
            for i in range(len(subset)):
                perms.append(subset[i])
                dfs(subset[:i] + subset[i+1:])
                perms.pop()
            
        dfs(nums)
        return list(res)