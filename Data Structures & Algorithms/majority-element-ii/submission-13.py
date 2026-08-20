class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            if len(counts) <= 2:
                continue
            new_counts = defaultdict(int)
            for key, value in counts.items():
                if value > 1:
                    new_counts[key] = value - 1
            counts = new_counts
        result = []
        for key in counts:
            if nums.count(key) > len(nums) // 3:
                result.append(key)
        return result