class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for i, e in enumerate(nums):
            diff = target - e
            if diff in pos:
                return [pos[diff], i]
                
            pos[e] = i 
        