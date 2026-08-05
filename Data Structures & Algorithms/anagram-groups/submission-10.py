class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = defaultdict(list)
        for string in strs:
            key = [0] * 26
            for char in string:
                key[ord(char) - ord('a')] += 1
            hashset[tuple(key)].append(string)
        return list(hashset.values())