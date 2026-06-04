class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s) - 1
        while lp < rp:
            if not s[lp].isalnum():
                lp += 1
            elif not s[rp].isalnum():
                rp -= 1
            elif s[lp].lower() != s[rp].lower():
                return False
            else:
                lp += 1
                rp -= 1
        return True