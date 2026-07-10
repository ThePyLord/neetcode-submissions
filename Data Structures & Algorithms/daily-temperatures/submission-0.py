class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stk = []
        for i in range(len(temperatures)):
            while stk and temperatures[i] > stk[-1][0]:
                sTemp, sIdx = stk.pop()
                res[sIdx] = i - sIdx
            stk.append((temperatures[i], i))
        return res