class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = max(nums)
        cur_max, cur_min = 1, 1

        for num in nums:
            tmp = num * cur_max
            cur_max = max(num * cur_max, num * cur_min, num)
            cur_min = min(tmp, num * cur_min, num)

            max_prod = max(max_prod, cur_max)
        
        return max_prod