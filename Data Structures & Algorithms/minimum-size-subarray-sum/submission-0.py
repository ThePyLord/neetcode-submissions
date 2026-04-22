class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = float('inf')
        l,r = 0, 0
        cur_sum = 0
        while r < len(nums):
            cur_sum += nums[r]
            while cur_sum >= target:
                cur_sum -= nums[l]
                best = min(best, r - l + 1)
                l += 1
            r += 1
        return 0 if best == float('inf') else best