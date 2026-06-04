class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxcount = 1
        count = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue
            if nums[i - 1] == (nums[i] - 1):
                count += 1
            else:
                if count > maxcount:
                    maxcount = count
                count = 1
        if count > maxcount:
            maxcount = count
        return maxcount