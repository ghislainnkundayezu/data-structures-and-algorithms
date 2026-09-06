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
    
    def merge(self, nums, l, r, m):
        left, right = nums[l : m+1], nums[m+1 : r+1]
        i, j, k = 0, 0, l

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            elif left[i] > right[j]:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i, k = i + 1, k + 1
        while j < len(right):
            nums[k] = right[j]
            j, k = j + 1, k + 1



