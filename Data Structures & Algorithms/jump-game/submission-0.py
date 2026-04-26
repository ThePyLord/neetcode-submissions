class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l, r = 0, len(nums) - 1
        for i in range(r-1, l - 1, -1):
            if nums[i] + i >= r:
                r = i
        return r <= l