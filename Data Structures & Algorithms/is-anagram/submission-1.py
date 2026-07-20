class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in hashmap_s:
                hashmap_s[s[i]] += 1
            else:
                hashmap_s[s[i]] = 1
            if t[i] in hashmap_t:
                hashmap_t[t[i]] += 1
            else:
                hashmap_t[t[i]] = 1
        return hashmap_s == hashmap_t