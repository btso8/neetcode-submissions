class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_sequence = 0
        for num in nums_set:
            if (num - 1) not in nums_set:
                current_sequence = 1
                while (num + 1) in nums_set:
                    current_sequence += 1
                    num = num + 1
                longest_sequence = max(current_sequence, longest_sequence)
        return longest_sequence