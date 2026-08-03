class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, left, middle, right):
            left_half = arr[left:middle+1]
            right_half = arr[middle+1:right+1]
            arr_index = left
            left_index = 0
            right_index = 0
            while left_index < len(left_half) and right_index < len(right_half):
                if left_half[left_index] <= right_half[right_index]:
                    arr[arr_index] = left_half[left_index]
                    left_index += 1
                else:
                    arr[arr_index] = right_half[right_index]
                    right_index += 1
                arr_index += 1
            while left_index < len(left_half):
                arr[arr_index] = left_half[left_index]
                left_index += 1
                arr_index += 1
            while right_index < len(right_half):
                arr[arr_index] = right_half[right_index]
                right_index += 1
                arr_index += 1

        def mergeSort(arr, left, right):
            if left == right:
                return arr
            middle = (left + right) // 2
            mergeSort(arr, left, middle)
            mergeSort(arr, middle + 1, right)
            merge(arr, left, middle, right)

        mergeSort(nums, 0, len(nums) - 1)
        return nums