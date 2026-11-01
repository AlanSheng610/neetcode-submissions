class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            a = ''.join(sorted(s))
            res[a].append(s)
        return list(res.values())