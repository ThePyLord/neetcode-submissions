class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        best = 0
        l, r = 0, 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            best = max(best, r - l + 1)
            char_set.add(s[r])
            r += 1

        return best