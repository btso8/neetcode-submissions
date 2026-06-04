class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numslength = len(nums)
        result = [0] * numslength
        for i in range(numslength):
            product = 1
            for j in range(numslength):
                if i != j:
                    product *= nums[j]
            result[i] = product
        return result