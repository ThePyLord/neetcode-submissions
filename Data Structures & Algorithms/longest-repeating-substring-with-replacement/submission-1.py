class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l = 0

        cnt = {}
        for r in range(len(s)):
            cnt[s[r]] = 1 + cnt.get(s[r], 0)

            while r - l + 1 - max(cnt.values()) > k:
                cnt[s[l]] -= 1
                l += 1
            max_len = max(r - l + 1, max_len)

        return max_len