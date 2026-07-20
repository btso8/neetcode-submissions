class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        return not len(nums) == len(numset)