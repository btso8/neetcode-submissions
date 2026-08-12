class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hashset = set(nums)
        longest_consecutive = 0
        for num in nums:
            if (num - 1) not in nums_hashset:
                count = 1
                while (num + count) in nums_hashset:
                    count += 1
                longest_consecutive = max(longest_consecutive, count)
        return longest_consecutive
