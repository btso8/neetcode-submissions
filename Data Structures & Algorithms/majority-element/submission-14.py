class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current = 0
        for num in nums:
            if current == 0:
                result = num
            if num == result:
                current += 1
            else:
                current -= 1
        return result