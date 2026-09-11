class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            
            if i-1 >= 0 and nums[i-1] == nums[i]:
                continue 

            l, r = i + 1, len(nums) - 1

            while l < r:
                tot = nums[i] + nums[l] + nums[r]

                if tot < 0:
                    l += 1
                elif tot > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while nums[l-1] == nums[l] and l < r:
                        l += 1
                        
        
        return res