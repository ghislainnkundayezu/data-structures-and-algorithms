class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums
    
    def mergeSort(self, nums, left, right):
        if left >= right:
            return
        
        mid = (left + right) // 2
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)
        
        # finally
        self.merge(nums, left, right, mid)
    
    def merge(self, arr, l, r, m):
        left, right = arr[l : m+1], arr[m+1 : r+1]
        i, j, k = 0, 0, l

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            elif left[i] > right[j]:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i, k = i + 1, k + 1
        while j < len(right):
            arr[k] = right[j]
            j, k = j + 1, k + 1



