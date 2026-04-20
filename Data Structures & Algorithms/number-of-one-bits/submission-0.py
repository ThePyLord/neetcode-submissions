class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_repr = bin(n)[2:]
        _sum = 0
        for char in bin_repr:
            if char == '1':
                _sum += 1
        return _sum
        