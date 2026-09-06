class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums)-1)
        return nums
    
    def mergeSort(self, nums, left, right):
        if left == right:
            print(left, right)
            return

        mid = (left+right)//2
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)

        self.merge(nums, left, right, mid)

    def merge(self, nums, left, right, mid):
        res = []
        l, r = left, mid + 1

        while l <= mid and r <= right:
            if nums[l] < nums[r]:
                res.append(nums[l])
                l += 1
            else:
                res.append(nums[r])
                r += 1
        
        while l <= mid:
            res.append(nums[l])
            l += 1
        
        while r <= right:
            res.append(nums[r])
            r += 1
        
        for k in range(len(res)):
            nums[left + k] = res[k]
        
