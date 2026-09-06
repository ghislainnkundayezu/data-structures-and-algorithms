class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for index, num in enumerate(nums):
            num_map[num] = index
    
        for n in range(len(nums)):
            diff = target - nums[n]
            if diff in num_map and num_map[diff] != n:
                return [n, num_map[diff]]
