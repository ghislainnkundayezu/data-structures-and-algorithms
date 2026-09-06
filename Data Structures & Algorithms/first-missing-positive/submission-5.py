class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1

        for _ in range(len(nums)):
            if res not in nums:
                return res   
            res += 1 
        
        return res