class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hmap = defaultdict(list)
        for s in strs:
            slist = sorted(s)
            key = tuple([ord(k) - ord('a') for k in slist])
            hmap[key].append(s)

        for key in hmap:
            res.append(hmap[key])
        return res