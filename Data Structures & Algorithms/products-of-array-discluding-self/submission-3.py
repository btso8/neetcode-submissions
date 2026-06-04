class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num
        if zero_count > 1:
            return [0] * len(nums)
        result = []
        for num in nums:
            if zero_count == 1:
                if num == 0:
                    result.append(total_product)
                else:
                    result.append(0)
            else:
                result.append(total_product // num)
        return result