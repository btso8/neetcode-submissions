class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l = 0
        r = 0
        longest = 0
        while r < len(s):
            if s[r] not in hashset:
                hashset.add(s[r])
                if len(hashset) > longest:
                    longest = len(hashset)
                r += 1
            else:
                hashset.remove(s[l])
                l += 1
        return longest