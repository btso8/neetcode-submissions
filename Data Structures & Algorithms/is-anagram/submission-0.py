class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hashmap = {}
        t_hashmap = {}
        for val in s:
            if val in s_hashmap:
                s_hashmap[val] += 1
            elif val not in s_hashmap:
                s_hashmap[val] = 1
        for val in t:
            if val in t_hashmap:
                t_hashmap[val] += 1
            elif val not in t_hashmap:
                t_hashmap[val] = 1
        if s_hashmap == t_hashmap:
            return True
        return False
