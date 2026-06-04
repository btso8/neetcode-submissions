import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        speed = r
        while l <= r:
            m = (l + r) // 2
            total = 0
            for pile in piles:
                total += math.ceil(float(pile) / m)
            if total <= h:
                speed = m
                r = m - 1
            else:
                l = m + 1
        return speed
            