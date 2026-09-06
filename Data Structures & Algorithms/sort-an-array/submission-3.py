class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, arr1, arr2):
        res = []
        l, r = 0, 0

        while l < len(arr1) and r < len(arr2):
            if arr1[l] < arr2[r]:
                res.append(arr1[l])
                l += 1
            else:
                res.append(arr2[r])
                r += 1

        if l < len(arr1):
            res.extend(arr1[l:])
        else:
            res.extend(arr2[r:])

        return res
