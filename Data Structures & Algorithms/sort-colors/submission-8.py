class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colours = [0] * 3
        for num in nums:
            colours[num] += 1
        index = 0
        for i in range(3):
            while colours[i]:
                nums[index] = i
                colours[i] -= 1
                index += 1