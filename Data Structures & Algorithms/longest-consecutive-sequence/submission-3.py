class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best_seq = 0
        num_set = list(set(nums))
        if len(nums) == 1: return 1
        for i in range(len(nums)):
            num = nums[i]
            if num in num_set: # Start sequence
                curr_seq = 0
                j = num
                while j in num_set:
                    j += 1
                    curr_seq += 1
                    best_seq = max(best_seq, curr_seq)

        return best_seq