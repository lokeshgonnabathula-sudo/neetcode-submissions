class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm=collections.defaultdict(list)
        for s in strs:
            key=str(sorted(list(s)))
            hm[key].append(s)
        return list(hm.values())