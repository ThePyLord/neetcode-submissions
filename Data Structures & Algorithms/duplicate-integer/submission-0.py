class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_table = {}
        for val in nums:
            if val not in freq_table:
                freq_table[val] = 1
            else:
                return True
        return False