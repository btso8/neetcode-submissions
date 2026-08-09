class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, l, m, r):
            left_side = arr[l : m + 1]
            right_side = arr[m + 1 : r + 1]
            left_index = 0
            right_index = 0
            arr_index = l
            while left_index < len(left_side) and right_index < len(right_side):
                if left_side[left_index] <= right_side[right_index]:
                    arr[arr_index] = left_side[left_index]
                    left_index += 1
                else:
                    arr[arr_index] = right_side[right_index]
                    right_index += 1
                arr_index += 1
            while left_index < len(left_side):
                arr[arr_index] = left_side[left_index]
                left_index += 1
                arr_index += 1
            while right_index < len(right_side):
                arr[arr_index] = right_side[right_index]
                right_index += 1
                arr_index += 1
        
        def merge_sort(arr, l, r):
            if l == r:
                return
            m = (l + r) // 2
            merge_sort(arr, l, m)
            merge_sort(arr, m + 1, r)
            merge(arr, l, m, r)

        merge_sort(nums, 0, len(nums) - 1)
        return nums