class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest_consecutive = 0
        for num in nums:
            if (num - 1) not in hashset:
                count = 1
                current = num + 1
                while current in hashset:
                    count += 1
                    current += 1
                longest_consecutive = max(longest_consecutive, count)
        return longest_consecutive