class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = nums[0]
        count = 1
        for num in nums[1:]:
            if num == result:
                count += 1
            else:
                count -= 1
            if count == 0:
                result = num
                count = 1
        return result