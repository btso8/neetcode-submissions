from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = defaultdict(list)
        for string in strs:
            sorted_str = "".join(sorted(string))
            sorted_strs[sorted_str].append(string)
        return list(sorted_strs.values())