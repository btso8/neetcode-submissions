class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(numbers)):
            othernum = target - numbers[i]
            if othernum in hashmap:
                return [hashmap[othernum] + 1, i + 1]
            else:
                hashmap[numbers[i]] = i