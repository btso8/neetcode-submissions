class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        window = {}
        countt = {}
        for val in t:
            countt[val] = countt.get(val, 0) + 1
        have = 0
        need = len(countt)
        result = [-1, -1]
        resultlen = float("infinity")
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in countt and window[s[r]] == countt[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < resultlen:
                    result = [l, r]
                    resultlen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countt and window[s[l]] < countt[s[l]]:
                    have -= 1
                l += 1
        if resultlen == float("infinity"):
            return ""
        return s[result[0] : result[1] + 1]