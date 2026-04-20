class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        
        res = []
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1
            
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res