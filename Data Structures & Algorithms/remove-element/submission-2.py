class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        k = len(nums)
        if len(nums) == 1 and nums[0] == val: return 0

        while l < r:
            #if nums[r] == val:
            #    r -= 1
            #    k -= 1
            #    continue
            while r>0 and nums[r] == val:
                r -= 1
                k -= 1
            
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l] 
                k -= 1
                r -= 1
            
            
            l += 1
        
        return k