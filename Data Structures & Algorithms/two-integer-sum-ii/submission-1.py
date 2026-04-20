class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        res = []
        for i in range(0, len(numbers)):
            for j in range(1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    # print(i, j)
                    res = [i + 1, j + 1]
                    return res
    
        return res