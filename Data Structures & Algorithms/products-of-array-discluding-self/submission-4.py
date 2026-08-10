class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1
        for i in range(1,len(result)):
            prefix *= nums[i-1]
            result[i] = prefix
        suffix = 1
        for i in range(len(result) - 2, -1, -1):
            suffix *= nums[i+1]
            result[i] *= suffix
        return result