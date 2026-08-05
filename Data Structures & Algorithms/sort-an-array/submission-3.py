class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr, l, m, r):
            left_side = arr[l:m+1]
            right_side = arr[m+1:r+1]
            left_pointer = 0
            right_pointer = 0
            arr_pointer = l
            while left_pointer < len(left_side) and right_pointer < len(right_side):
                if left_side[left_pointer] <= right_side[right_pointer]:
                    arr[arr_pointer] = left_side[left_pointer]
                    left_pointer += 1
                else:
                    arr[arr_pointer] = right_side[right_pointer]
                    right_pointer += 1
                arr_pointer += 1
            while left_pointer < len(left_side):
                arr[arr_pointer] = left_side[left_pointer]
                left_pointer += 1
                arr_pointer += 1
            while right_pointer < len(right_side):
                arr[arr_pointer] = right_side[right_pointer]
                right_pointer += 1
                arr_pointer += 1
        
        def mergeSort(arr, l, r):
            if l == r:
                return
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
        
        mergeSort(nums, 0, len(nums) - 1)
        return nums