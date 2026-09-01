class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            if len(counts) <= 2:
                continue
            new_counts = defaultdict(int)
            for n, count, in counts.items():
                if count > 1:
                    new_counts[n] = count - 1
            counts = new_counts
        result = []
        for num in counts:
            if nums.count(num) > len(nums) // 3:
                result.append(num)
        return result